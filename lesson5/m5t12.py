import re


def replace_spam_words(text, spam_words):
    for word in spam_words:
        text = re.sub(word, '*'*len(word), text, flags=re.IGNORECASE)       
    return text

