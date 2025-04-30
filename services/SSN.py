from services.Valadation import Validation

class SSN:
    def __init__(self, contex, Format):
        self.validator = Validation(contex, Format)  # תיקון כתיב

    def CheckValidation_ssn(self, text):
        ans = self.validator.sensetive_text_ssn_credit(text)
        if ans == 1:
            return "found credit number"  # תיקון כתיב
        if ans == 2:
            return "found sensitive data"  # תיקון כתיב
        return "no sensitive data found"  # הוספת טיפול ברירת מחדל
