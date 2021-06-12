CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS,TRANSLATION):    
    TRANS[ord(c.upper())] = l.upper()
    TRANS[ord(c)] = l


def translate(name):
    return name.translate(TRANS)
    

print(TRANS)
print('картошка'.translate(TRANS))
print(translate('пирожок'))