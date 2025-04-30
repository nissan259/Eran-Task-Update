import unittest
import json
from server import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.username = "test_user"
        self.password = "test123"
        self.email = "test@example.com"

    def test_1_register_user(self):
        response = self.client.post("/auth/register", json={
            "username": self.username,
            "password": self.password,
            "email": self.email
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("token", data)
        self.token = data["token"]

    def test_2_login_user(self):
        response = self.client.post("/auth/login", json={
            "username": self.username,
            "password": self.password
        })
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("token", data)
        self.token = data["token"]

    def test_3_detect_ssn(self):
        # קודם נבצע login כדי לקבל טוקן
        login_response = self.client.post("/auth/login", json={
            "username": self.username,
            "password": self.password
        })
        token = login_response.get_json()["token"]

        detect_response = self.client.post("/dlp/detect",
            headers={"Authorization": f"Bearer {token}"},
            json={
                "type": "ssn",
                "text": "my ssn is 123-45-6789"
            }
        )
        self.assertEqual(detect_response.status_code, 200)
        data = detect_response.get_json()
        self.assertIn("result", data)
        self.assertEqual(data["result"], "sensitive")

if __name__ == '__main__':
    unittest.main()
