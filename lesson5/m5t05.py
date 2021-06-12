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


def get_phone_numbers_for_countries(list_phones):
    phone_dict = {'JP':[],'SG':[], 'TW':[], 'UA':[]}
    for phone in list_phones:
        if sanitize_phone_number(phone).startswith('81'):
            phone_dict['JP'].append(sanitize_phone_number(phone))
        if sanitize_phone_number(phone).startswith('65'):
            phone_dict['SG'].append(sanitize_phone_number(phone))
        if sanitize_phone_number(phone).startswith('886'):
            phone_dict['TW'].append(sanitize_phone_number(phone))
        if sanitize_phone_number(phone).startswith('380'):
            phone_dict['UA'].append(sanitize_phone_number(phone))
    return phone_dict

print(get_phone_numbers_for_countries(['+380632555123','+812356874','+654557841','+8865214532','+380632555124', '+380632555125']))