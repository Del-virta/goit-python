import random
def random_winners(count, user_dict):
    try:
        keys_list = list(user_dict.keys())
        random.shuffle(keys_list)        
        return random.sample(keys_list, k=count)
    except ValueError:
        print(f"Число {count} превышает количество участников {len(user_dict)}")

print(random_winners(2, {"Oleg": 1362, "Anna": 3295, "Ira": 1234, "Boris": 3333}))