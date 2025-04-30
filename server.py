from flask import Flask
from dotenv import load_dotenv
from routes.auth_routes import auth_bp
from routes.dlp_routes import dlp_bp

# טען משתני סביבה מה־.env
load_dotenv()

# יצירת אפליקציית Flask
app = Flask(__name__)

# רישום Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dlp_bp, url_prefix="/dlp")

# נקודת כניסה להרצת השרת
if __name__ == "__main__":
    app.run(debug=True)
