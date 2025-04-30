FORMAT_PRESETS = {
    "ssn": "ddd-dd-dddd",
    "credit_card": "dddd dddd dddd dddd",
    "iban": "ILkk bbbb ssss ssss ssss sss",
    "israeli_id": "ddddddddd"
}

def get_format_by_type(type_name):
    return FORMAT_PRESETS.get(type_name.lower())
