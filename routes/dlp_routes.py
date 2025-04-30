from flask import Blueprint, request, jsonify
from services.regex_pattern import RegexBuilder
from utils.auth_decorators import require_auth
from models.Requast_model import set_request  # ← כאן אתה משתמש בפונקציה שלך
import re

dlp_bp = Blueprint("dlp", __name__)

@dlp_bp.route('/detect', methods=['POST'])
@require_auth
def detect_sensitive_data():
    data = request.get_json()
    text = data.get("text")
    data_type = data.get("type")
    username = request.user.get("username")

    # שימוש ב־set_request לאימות ולשמירה במסד
    request_result = set_request({
        "checktype": data_type,
        "text": text
    }, username)

    if "error" in request_result:
        return jsonify(request_result), 400

    # אם זה IBAN → טיפול ייעודי
    if data_type.lower() == "iban":
        pattern = RegexBuilder.build_iban_regex()
        match = re.findall(pattern, text)
        result = "sensitive" if match else "not_sensitive"
    else:
        format_str = RegexBuilder.get_preset_format(data_type)
        if not format_str:
            return jsonify({"error": f"Unsupported type '{data_type}'"}), 400

        pattern = RegexBuilder.format_to_regex(format_str)
        match = re.findall(pattern, text)
        result = "sensitive" if match else "not_sensitive"

    return jsonify({
        "request_id": str(request_result["_id"]),
        "username": username,
        "type": data_type,
        "match": bool(match),
        "result": result
    })
