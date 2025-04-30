import os
from dotenv import load_dotenv

load_dotenv()

def load_config():
    return {
        "MONGO_URI": os.getenv("MONGO_URI"),
        "JWT_SECRET": os.getenv("SECRET_KEY"),
        "JWT_EXP_MINUTES": int(os.getenv("JWT_EXP_MINUTES", 60))
    }
