import unittest
import os
from server import app
from db import db

os.environ["TESTING"] = "1"

class TestAppWithMongoMock(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.username = "test_user"
        self.password = "123456"
        self.email = "test@example.com"

        # רישום משתמש חדש (אם לא נרשם עדיין)
        self.client.post("/auth/register", json={
            "username": self.username,
            "password": self.password,
            "email": self.email
        })

    def get_token(self):
        res = self.client.post("/auth/login", json={
            "username": self.username,
            "password": self.password
        })
        return res.get_json()["token"]

    def test_register_duplicate(self):
        res = self.client.post("/auth/register", json={
            "username": self.username,
            "password": self.password,
            "email": self.email
        })
        self.assertEqual(res.status_code, 400)
        self.assertIn("error", res.get_json())

    def test_login_success(self):
        res = self.client.post("/auth/login", json={
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn("token", res.get_json())

    def test_detect_ssn(self):
        token = self.get_token()
        res = self.client.post("/dlp/detect",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "type": "ssn",
                "text": "my ssn is 123-45-6789"
            }
        )
        self.assertEqual(res.status_code, 200)
        data = res.get_json()
        self.assertEqual(data["result"], "sensitive")

    def test_detect_invalid_token(self):
        res = self.client.post("/dlp/detect",
            headers={"Authorization": "Bearer fake_token"},
            json={"type": "ssn", "text": "123-45-6789"}
        )
        self.assertEqual(res.status_code, 401)

    def test_detect_credit_card(self):
        token = self.get_token()
        res = self.client.post("/dlp/detect",
            headers={"Authorization": f"Bearer {token}"},
            json={"type": "credit_card", "text": "card 1234 5678 1234 5670"}
        )
        self.assertEqual(res.status_code, 200)
        self.assertIn("result", res.get_json())

    def test_detect_invalid_type(self):
        token = self.get_token()
        res = self.client.post("/dlp/detect",
            headers={"Authorization": f"Bearer {token}"},
            json={"type": "passport", "text": "AB1234567"}
        )
        self.assertEqual(res.status_code, 400)

if __name__ == "__main__":
    unittest.main()
