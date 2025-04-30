from flask import request, jsonify
from utils.jwt_handler import decode_jwt
from functools import wraps

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers.get("Authorization")
        if not auth or not auth.startswith("Bearer "):
            return jsonify({"error": "Missing token"}), 401

        token = auth.split(" ")[1]
        try:
            decoded = decode_jwt(token)
            request.user = decoded  # שמירה זמנית של פרטי המשתמש
        except Exception:
            return jsonify({"error": "Invalid token"}), 401

        return f(*args, **kwargs)
    return wrapper
