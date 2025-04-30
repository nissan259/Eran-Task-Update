
# 🔐 DLP API – Data Leakage Detection

A Flask-based API to detect sensitive data (SSNs, credit cards, IBANs) using regex patterns and checksums.  
Includes user authentication, JWT protection, and MongoDB integration.

## 🚀 Features

- User registration & login with JWT
- Protected endpoints for sensitive text detection
- Regex-based format matching
- Luhn and IBAN checksum validation
- MongoDB (mockable with `mongomock`)
- Ready for unit & integration testing

## 📦 Tech Stack

- Python 3.x + Flask
- PyJWT, bcrypt, pymongo
- MongoDB / mongomock
- Unittest for test coverage

## 🛠️ Setup

```bash
git clone https://github.com/your-user/dlp-api.git
cd dlp-api
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```ini
MONGO_URI=your_mongo_uri
SECRET_KEY=your_secret_key
JWT_EXP_MINUTES=120
```

Run the app:

```bash
python server.py
```

## ✅ Running Tests

```bash
export TESTING=1  # or set TESTING=1 on Windows
python test_routes.py
python test_logic.py
```

## 📁 Project Structure

- `routes/` – API endpoints
- `models/` – Business logic
- `services/` – Regex + validation logic
- `utils/` – JWT, password, decorators
- `db.py` – Mongo client
- `tests/` – Unittests with mongomock

---

Made with ❤️ by Orel Nisan
