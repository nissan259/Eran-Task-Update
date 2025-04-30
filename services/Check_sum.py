class Checksum:
    def Luhn_checksum(self, cardNumber):
        sum = 0
        length = len(cardNumber)
        parity = (length - 1) % 2
        check_digit = int(cardNumber[-1])
        main_digits = cardNumber[:-1]

        for i in range(len(main_digits)):
            digit = int(main_digits[i])
            if i % 2 == parity:
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum += digit

        calculated_check = (10 - (sum % 10)) % 10
        return check_digit == calculated_check

    def IBAN_checksum(self, iban_code):
        code = iban_code.strip()
        country_code_to_find = code[0:2]

        try:
            with open("country_iban_lengths.txt", "r") as file:
                iban_length = None
                for line in file:
                    country_code, length = line.strip().split()
                    if country_code == country_code_to_find:
                        iban_length = int(length)
                        break
        except FileNotFoundError:
            return False

        if iban_length is None:
            return False
        if len(code) != iban_length:
            return False

        iban_code = code[4:] + code[0:4]

        result = ""
        for char in iban_code:
            if char.isdigit():
                result += char
            elif char.isalpha():
                numeric_value = str(ord(char.upper()) - 55)
                result += numeric_value

        result = int(result)
        const_split_iban = 97
        remainder = result % const_split_iban

        return remainder == 1
