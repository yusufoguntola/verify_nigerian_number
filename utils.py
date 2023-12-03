def format_as_key(val):
    pass


def format_to_11_digit(msisdn):
    temp = str(msisdn).strip()
    if temp.startswith("+2340"):
        temp = f"0{temp[5:]}"
    elif temp.startswith("+234") or temp.startswith("2340"):
        temp = f"0{temp[4:]}"
    elif temp.startswith("234"):
        temp = f"0{temp[3:]}"
    elif len(temp) == 10:
        temp = f"0{temp}"
    return temp


def internationalize_number(msisdn):
    return f"234{format_to_11_digit(msisdn)[1:]}"
