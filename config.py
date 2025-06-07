import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables desde .env

# JWT secret para firmar y verificar tokens
JWT_SECRET = os.getenv("JWT_SECRET")
if not JWT_SECRET:
    raise ValueError("JWT_SECRET is not set in the environment variables.")

# Configuración de la base de datos PostgreSQL
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", 5432)),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# Verifica que todas las variables necesarias estén presentes
for key, value in DB_CONFIG.items():
    if value is None:
        raise ValueError(f"Missing required DB_CONFIG environment variable: {key}")
