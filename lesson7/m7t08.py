import re
def token_parser(s):
    new_s = re.split(r'([+-/*()])',s)
    for i in range(len(new_s)):
        if len(new_s[i])>=1:
            new_s[i] = new_s[i].strip()
    newest_s = []
    for item in new_s:
        if len(item)<1:
            pass
        else:
            newest_s.append(item)
    return newest_s
print(token_parser('(2+ 3) *45 - 5 * 3'))