def real_len(text):
    t_length = 0
    for char in text:      
        if char in ['\v','\n','\t','\r','\f']:
            pass
        else:
            t_length+=1
    return t_length

text = 'Мы думали над тем, как можно все бросить и удететь в космос.\nГде-то там останется семья и друзья. \v а ты сидишь и смотришь в глубокую синеву день за днем.'
print(real_len(text))
print(len(text))