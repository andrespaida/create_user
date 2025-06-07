from flask import Flask
from flask_cors import CORS
from routes import routes

app = Flask(__name__)
CORS(app)  # 👈 Habilita CORS para todos los dominios

app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
