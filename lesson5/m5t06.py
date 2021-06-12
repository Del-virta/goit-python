def is_spam_words(text, spam_words, space_around=False):
    if space_around == False:
        for word in spam_words:
            if text.lower().find(word.lower()) != -1:
                return True
            else:
                return False
    else:
        for word in spam_words:
            if text.lower().find(' '+word.lower()) != -1 or text.lower().find('.'+word.lower()) != -1:
                return True
            else:
                return False

print(is_spam_words("Молох", ["лох"]))  
print(is_spam_words("Молох", ["лох"], True))