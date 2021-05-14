def is_integer(s):
    strip_s = s.strip()
    if strip_s[0] in ['+','-']:
        if strip_s[1:].isdigit(): return True
    elif strip_s.isdigit():
        return True
    else: return False

print(is_integer('+34'))