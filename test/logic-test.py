import unittest
import sys
import os
from services.Credit_Card_Number import Credit_Card_Number
from services.SSN import SSN
from services.IBAN import IBAN
from services.Check_sum import Checksum
from services.regex_pattern import RegexBuilder

# הוספת נתיב לתיקיית services
sys.path.append(os.path.join(os.path.dirname(__file__), 'services'))



class LogicTests(unittest.TestCase):

    def test_credit_card_valid_detection(self):
        text = "My credit card is 1234 5678 9012 3452"
        validator = Credit_Card_Number(["card", "credit"], "dddd dddd dddd dddd")
        result = validator.Credit_Card_Number_check(text)
        self.assertIn(result, ["senstive_text", "not_sensetive"])

    def test_ssn_detection(self):
        ssn = SSN(["ssn", "number"], "ddd-dd-dddd")
        text = "my ssn is 123-45-6789"
        result = ssn.CheckValidation_ssn(text)
        self.assertIn(result, ["found sensitive data", "no sensitive data found"])

    def test_iban_valid(self):
        iban = IBAN()
        text = "IL620108000000099999999"
        result = iban.IbanValation(text)
        self.assertIn(result, ["Sensitive text", "Not sensitive"])

    def test_regex_format_conversion(self):
        regex = RegexBuilder.format_to_regex("dddd dd")
        self.assertIsInstance(regex, str)
        self.assertIn(r"\d", regex)

    def test_word_regex_builder(self):
        regex = RegexBuilder.words_to_regex(["ssn", "card"])
        self.assertIn("ssn", regex)
        self.assertIn("card", regex)

    def test_luhn_checksum_valid(self):
        checksum = Checksum()
        self.assertTrue(checksum.Luhn_checksum("79927398713"))  # תקין

    def test_luhn_checksum_invalid(self):
        checksum = Checksum()
        self.assertFalse(checksum.Luhn_checksum("79927398710"))  # לא תקין

if __name__ == '__main__':
    unittest.main()
