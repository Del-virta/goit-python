def solve_riddle(riddle, word_length, start_letter, reverse=False):
    start_letter_idx = riddle.find(start_letter)
    if reverse == False:
        result = riddle[start_letter_idx:start_letter_idx+word_length]
    else:
        result = riddle[start_letter_idx:start_letter_idx - word_length:-1]
    return result

print(solve_riddle('атмтертропкра',7,'п',reverse=True))