
from flask import Blueprint, request, jsonify
from models.user_model import login_user, register_user
from utils.jwt_handler import generate_jwt


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = register_user(data)
    if isinstance(user, dict) and "error" in user:
        return jsonify(user), 400
    token = generate_jwt(user)
    return jsonify({"token": token})


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = login_user(data)
    if isinstance(user, dict) and "error" in user:
        return jsonify(user), 401

    token = generate_jwt(user)
    return jsonify({"token": token})
