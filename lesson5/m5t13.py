import re


def find_all_emails(text):
    result = re.findall(r'[a-zA-Z][\w\._]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}', text)
    return result

