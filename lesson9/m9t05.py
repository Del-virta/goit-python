def format_phone_number(func):
    def inner(phone):
        if len(phone)<12:
            return '+38' + func(phone)
        else:
            return '+' + func(phone)
    return inner  

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number('0503451234'))