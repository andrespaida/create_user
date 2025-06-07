from flask import Blueprint, request, jsonify
from db import get_db_connection
from models import create_user
from utils import hash_password, verify_token
import jwt  # ⬅️ Necesario para capturar excepciones correctamente

routes = Blueprint('routes', __name__)

@routes.route('/users/create', methods=['POST'])
def create_user_route():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    name = data.get('name', '')  # Por si se usa en futuro, aunque no esté en frontend aún
    email = data.get('email')
    password = data.get('password')
    role = data.get('role', 'user')  # 'user' por defecto

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    # ⚠️ Validar si se intenta crear admin
    if role == 'admin':
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Admin role requires authentication"}), 401

        try:
            token = auth_header.split()[1]
            decoded = verify_token(token)

            if decoded.get('role') != 'admin':
                return jsonify({"error": "Only admins can create other admins"}), 403

        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Invalid token"}), 401

    password_hash = hash_password(password)

    try:
        conn = get_db_connection()
        create_user(conn, name or email, email, password_hash, role)
        conn.close()
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
