def sequence_buttons(string):
    phone_dict = {
            1: ['.', ',', '?', '!', ':'],
            2: ['A', 'B', 'C'],
            3: ['D', 'E', 'F'],
            4: ['G', 'H', 'I'],
            5: ['J', 'K', 'L'],
            6: ['M', 'N', 'O'],
            7: ['P', 'Q', 'R', 'S'],
            8: ['T', 'U', 'V'],
            9: ['W', 'X', 'Y', 'Z'],
            0: [' ']
        }
    result = ''
    for char in string:
        for key, value in phone_dict.items():
            if char.upper() in value:
               result += f'{key}' * (value.index(char.upper()) + 1)
    return result

print(sequence_buttons('Hello, world!'))