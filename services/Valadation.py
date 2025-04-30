import re
from services.regex_pattern import RegexBuilder

class Validation:
    def __init__(self, _format, context_words):
        self.format = _format
        self.context_words = context_words

    def get_format_regex(self):
        return RegexBuilder.format_to_regex(self.format)

    def get_words_regex(self):
        return RegexBuilder.words_to_regex(self.context_words)

    def sensitive_text_ssn_credit(self, text):
        number_match = 0
        pattern_context = self.get_words_regex()
        pattern_credit_card_format = self.get_format_regex()

        match_context = re.findall(pattern_context, text)
        match_credit_card = re.findall(pattern_credit_card_format, text)

        if match_credit_card:
            number_match += 1
        if match_context:
            number_match += 1

        return number_match, match_credit_card

    def sensitive_text_iban(self, text):
        pattern = RegexBuilder.build_iban_regex()
        match = re.findall(pattern, text)
        if match:
            return match
        return None
