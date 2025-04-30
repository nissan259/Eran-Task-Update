import jwt
import datetime
from config import load_config

config = load_config()
SECRET = config["JWT_SECRET"]
EXP_MINUTES = config["JWT_EXP_MINUTES"]

# בדיקה שהמפתח תקין
if not SECRET or not isinstance(SECRET, str):
    raise ValueError("Invalid or missing JWT_SECRET in config")

def generate_jwt(user):
    payload = {
        "user_id": str(user["_id"]),
        "username": user["username"],
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=EXP_MINUTES)
    }

    token = jwt.encode(payload, SECRET, algorithm="HS256")

    # במידה והספרייה מחזירה bytes (גרסאות ישנות)
    if isinstance(token, bytes):
        token = token.decode("utf-8")

    return token

def decode_jwt(token):
    return jwt.decode(token, SECRET, algorithms=["HS256"])
