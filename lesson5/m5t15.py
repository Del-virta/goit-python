import re


def find_all_links(text):
    result = []
    iterator = re.finditer(r'(https?://[a-zA-Z0-9_]+\.{,1}[a-zA-Z0-9_]+\.[a-zA-Z]{3,})', text)
    for match in iterator:
        result.append(match.group())
    return result