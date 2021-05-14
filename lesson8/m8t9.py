def modify_lists(list_for_dict, pow_dict, list_for_list, add_num):
    new_list = [i+add_num for i in list_for_list]
    new_dict = {i:i**pow_dict for i in list_for_dict}
    return (new_dict, new_list)

print(modify_lists([1,3],2,[3,5],7))