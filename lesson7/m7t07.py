def data_preparation(list_data):
    new_list = []
    for each_list in list_data:
        if len(each_list)>2:
            sorted_list = sorted(each_list)
            sorted_list.pop(0)
            sorted_list.pop(-1)
            new_list.extend(sorted_list)
        else:
            new_list.extend(each_list)
    return sorted(new_list,reverse=True)
print(data_preparation([[1,2,3],[3,4], [5,6]]))