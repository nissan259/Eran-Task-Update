from db import db
from datetime import datetime

ALLOWED_TYPES = ["ssn", "iban", "credit_card"]

def set_request(data, username):
    checktype = data.get("checktype")
    text = data.get("text")

    if not all([checktype, text]):
        return {"error": "Missing fields"}

    if checktype not in ALLOWED_TYPES:
        return {"error": "Invalid check type"}

    # כאן נבדוק אם המשתמש קיים
    if not db.users.find_one({"username": username}):
        return {"error": "Invalid username"}

    request = {
        "username": username,
        "checktype": checktype,
        "text": text,
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    try:
        inserted = db.requests.insert_one(request)
        request["_id"] = inserted.inserted_id
        return request
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
