
import re
def capital_text(s):
    strip_s = s.lstrip()
    cap_first = strip_s[0].upper()+strip_s[1:]
    sentences = re.split(r'([?!.])', cap_first)
    new_sentences = []
    for sentence in sentences:
        new_sentence = sentence.strip()
        if len(new_sentence)>1:
            new_sentences.append(new_sentence[0].upper()+new_sentence[1:])
        else:
            new_sentences.append(new_sentence+' ')
        new_s = new_sentences[0]+''.join(new_sentences[1:])
    return new_s
print(capital_text('  hello! who are you? i think I know you. but I am not sure.'))