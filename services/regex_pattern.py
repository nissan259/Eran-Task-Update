import re

class RegexBuilder:
    FORMAT_PRESETS = {
        "ssn": "ddd-dd-dddd",
        "credit_card": "dddd dddd dddd dddd",
        "israeli_id": "ddddddddd",
        "iban": "ILdd bbbb ssss ssss ssss sss",
        "amex": "dddd dddddd ddddd"
    }

    @classmethod
    def get_preset_format(cls, type_name):
        return cls.FORMAT_PRESETS.get(type_name.lower())

    @staticmethod
    def format_to_regex(format_string):
        """המרת פורמט כללי (כמו dddd dd) ל-Regex חכם"""
        regex = ""
        for char in format_string:
            if char == 'd':
                regex += r'\d'
            elif char == ' ':
                regex += r'\s'
            else:
                regex += re.escape(char)

        # קיבוץ ספרות ורווחים רציפים
        regex = re.sub(r'(\\d)+', lambda m: f'\\d{{{len(m.group(0)) // 2}}}', regex)
        regex = re.sub(r'(\\s)+', lambda m: f'\\s{{{len(m.group(0)) // 2}}}', regex)
        return regex

    @staticmethod
    def words_to_regex(words_list):
        """בניית ביטוי רגולרי מתוך רשימת מילים"""
        escaped_words = [re.escape(word) for word in words_list]
        regex = r'\b(?:' + '|'.join(escaped_words) + r')\b'
        return regex

    @staticmethod
    def load_country_codes(file_path):
        """טעינת קודי מדינות לקובץ רשימה"""
        with open(file_path, 'r') as file:
            country_codes = [line.strip().lower() for line in file if line.strip()]
        return country_codes

    @staticmethod
    def build_iban_regex(file_path='services/country_code_iban_lengths.txt'):
        """בניית Regex דינמי לאימות IBAN על בסיס קובץ קוד מדינות"""
        country_codes = RegexBuilder.load_country_codes(file_path)
        pattern = r'^(' + '|'.join(re.escape(code) for code in country_codes) + r')'
        pattern += r'[0-9]{2}\s?([a-zA-Z0-9]{4}\s?){1,7}[a-zA-Z0-9]{1,3}$'
        return re.compile(pattern, re.IGNORECASE)
