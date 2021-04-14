import re

def normalize(text):
    symbol_map = {ord('А'): "A",
    ord('Б'): "B",
    ord('В'): "V",
    ord('Г'): "G",
    ord('Д'): "D",
    ord('Е'): "E",
    ord('Ё'): "Yo",
    ord('Ж'): "Zh",
    ord('З'): "Z",
    ord('И'): "I",
    ord('Й'): "Y",
    ord('К'): "K",
    ord('Л'): "L",
    ord('М'): "M",
    ord('Н'): "N",
    ord('О'): "O",
    ord('П'): "P",
    ord('Р'): "R",
    ord('С'): "S",
    ord('Т'): "T",
    ord('У'): "U",
    ord('Ф'): "F",
    ord('Х'): "Kh",
    ord('Ц'): "Ts",
    ord('Ч'): "Ch",
    ord('Ш'): "Sh",
    ord('Щ'): "Shch",
    ord('Э'): "E",
    ord('Ю'): "Yu",
    ord('Я'): "Ya",
    ord('Ы'): "I",
    ord('Ь'): "'",
    ord('Ъ'): "",
    ord('a'): "a",
    ord('б'): "b",
    ord('в'): "v",
    ord('г'): "g",
    ord('д'): "d",
    ord('е'): "e",
    ord('ё'): "yo",
    ord('ж'): "zh",
    ord('з'): "z",
    ord('и'): "i",
    ord('й'): "y",
    ord('к'): "k",
    ord('л'): "l",
    ord('м'): "m",
    ord('н'): "n",
    ord('о'): "o",
    ord('п'): "p",
    ord('р'): "r",
    ord('с'): "s",
    ord('т'): "t",
    ord('у'): "u",
    ord('ф'): "f",
    ord('х'): "kh",
    ord('ц'): "ts",
    ord('ч'): "ch",
    ord('ш'): "sh",
    ord('щ'): "shch",
    ord('э'): "e",
    ord('ю'): "yu",
    ord('я'): "ya",
    ord('ы'): "i",
    ord('ь'): "'",
    ord('ъ'): ""}
    text_with_no_symbols = re.sub("\W", "_", text)
    fixed_text = text_with_no_symbols.translate(symbol_map)
    return fixed_text


def main():
    text = input("Ведите текст для обработки: ")
    print(normalize(text))


if __name__ == "__main__":
    main()