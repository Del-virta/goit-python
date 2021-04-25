import re
def get_ingredients(path, position_name):
    with open(path,'r') as fh:    
        for position in fh.readlines():
            if re.search(position_name,position):
                the_line = position.split(':')
                ingredients = the_line[1]
                ing_list = ingredients.split(',')
    return ing_list