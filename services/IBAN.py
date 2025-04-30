from services.Valadation import Validation
from services.Check_sum import Checksum

class IBAN:
    def __init__(self):
        self.validator = Validation("", "")  # תיקון כתיב
        self.checksum = Checksum()

    def IbanValation(self, text):
        match = self.validator.sensetive_text_iban(text)
        if match is not None:
            for credit in match:
                if self.checksum.IBAN_checksum(credit):
                    return "Sensitive text"  # תיקון כתיב
            return "Not sensitive"  # במקרה שאין IBAN תקין
        else:
            return "Not sensitive"  # גם אם אין התאמות בכלל
