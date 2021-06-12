import re


def find_word(text, word):
    result = {}
    search_line = re.search(word, text)
    if re.search(word, text)!=None:
        result['result'] = True
        result['first_index'] = search_line.start()
        result['last_index'] = search_line.end()
        result['search_string'] = word
        result['string'] = text
    else:
        result['result'] = False
        result['first_index'] = None
        result['last_index'] = None
        result['search_string'] = word
        result['string'] = text
    return result

print(find_word('Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language', 'late'))