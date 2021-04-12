def format_ingredients(items):
    ingredients = []
    if len(items) > 1:
        for i in items[0:-2]:
            i+=", "
            ingredients.append(i)
        item = items[-2] + ' и ' + items[-1]
        ingredients.append(item)
        result = ''.join(ingredients)
    else:
        result = ''.join(items)
    return result
items = ['яйца 2шт', 'сахар 1 л.', 'соль 1 чл.', 'уксус']
print(format_ingredients(items))
