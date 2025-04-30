from db import db
from utils.hash_utils import hash_password
import re
from datetime import datetime
from utils.hash_utils import verify_password


EMAIL_REGEX = r'^\S+@\S+\.\S+$'

def register_user(data):
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")

    # בדיקה ששדות קיימים
    if not all([username, password, email]):
        return {"error": "Missing fields"}

    # בדיקת פורמט של כתובת אימייל
    if not re.match(EMAIL_REGEX, email):
        return {"error": "Invalid email address"}

    # בדיקת שם משתמש כפול
    if db.users.find_one({"username": username}):
        return {"error": "Username already exists"}

    # בדיקת כתובת אימייל כפולה
    if db.users.find_one({"email": email}):
        return {"error": "Email already in use"}

    # יצירת משתמש חדש
    user = {
        "username": username,
        "email": email,
        "password": hash_password(password),
        "role": "user",
        "created_at": datetime.utcnow()
    }

    try:
        inserted = db.users.insert_one(user)
        user["_id"] = inserted.inserted_id
        return user
    except Exception as e:
        return {"error": f"Database error: {str(e)}"}
def login_user(data):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"error": "Missing credentials"}

    user = db.users.find_one({"username": username})
    if not user:
        return {"error": "Invalid username or password"}

    if not verify_password(password, user["password"]):
        return {"error": "Invalid username or password"}

    return user