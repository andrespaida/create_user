import bcrypt
import jwt
from config import JWT_SECRET

def hash_password(password: str) -> str:
    """Hash the password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_token(token: str) -> dict:
    """
    Decode a JWT token and return its payload.
    Raises jwt.ExpiredSignatureError or jwt.InvalidTokenError if invalid.
    """
    return jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
