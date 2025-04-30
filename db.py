import os

if os.getenv("TESTING") == "1":
    import mongomock
    client = mongomock.MongoClient()
else:
    from pymongo import MongoClient
    from config import load_config
    config = load_config()
    client = MongoClient(config["MONGO_URI"])

db = client["dlp"]  # שנה לשם הדאטאבייס שלך
