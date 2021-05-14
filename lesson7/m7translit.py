CYRILLIC = ("а", "ч", "ш")
LATIN = ("a", "ch", "sh")

TRANSLIT_DICT = {}

for c, l in zip(CYRILLIC, LATIN):
    TRANSLIT_DICT[ord(c)] = l
    TRANSLIT_DICT[ord(c.upper())] = l.upper()

print("чаша".translate(TRANSLIT_DICT))  # chasha
print("ЧАША".translate(TRANSLIT_DICT))  # CHASHA