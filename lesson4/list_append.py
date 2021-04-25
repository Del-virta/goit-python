my_list_1 = []
my_list_2 = []
symbols = ['3','339','2','22','4','44','5','6']
for item in symbols:
    if len(item)<2:
        my_list_1+=item
    else:
        my_list_2+=item
print(my_list_1)
print(my_list_2)
