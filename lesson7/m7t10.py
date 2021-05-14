def make_request(keys, values):
    new_dict = {}
    if len(keys)!=len(values):
        pass
    else:
        for i in range(len(keys)):      
            new_dict[keys[i]] = values[i]
    return new_dict
print(make_request(['lang','python','salary','1500'],['class','middle','key','value']))
