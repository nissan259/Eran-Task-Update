from flask import Blueprint, request, jsonify
from services.pattern_resolver import get_pattern_handler
from utils.auth_decorators import require_auth
from models.request_model import set_request  # ← תיקון שם

dlp_bp = Blueprint("dlp", __name__)

@dlp_bp.route('/detect', methods=['POST'])
@require_auth
def detect_sensitive_data():
    data = request.get_json()
    text = data.get("text")
    data_type = data.get("type")
    username = request.user.get("username")

    if not text or not data_type:
        return jsonify({"error": "Missing text or type"}), 400

    request_result = set_request({
        "checktype": data_type,
        "text": text
    }, username)

    if "error" in request_result:
        return jsonify(request_result), 400

    # כאן השינוי העיקרי – שימוש במחלקות ולא ב־if/else
    pattern_handler = get_pattern_handler(data_type)
    if not pattern_handler:
        return jsonify({"error": f"Unsupported type '{data_type}'"}), 400

    is_sensitive = pattern_handler.match(text)

    return jsonify({
        "request_id": str(request_result["_id"]),
        "username": username,
        "type": data_type,
        "match": is_sensitive,
        "result": "sensitive" if is_sensitive else "not_sensitive"
    }), 200
