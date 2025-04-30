from services.Valadation import Validation
from services.Check_sum import  Checksum


class Credit_Card_Number:
    def __init__(self,contex,formats):
        self.valditor=Validation(contex,formats)
        self.checksum=Checksum()

    def Credit_Card_Number_check(self,text):
        number_match, matched_cards = self.valditor.sensitive_text_ssn_credit(text)
        if number_match == 2 and matched_cards and self.checksum.Luhn_checksum(matched_cards[0]):
            return "senstive_text"
        else:
            return "not_sensetive"





