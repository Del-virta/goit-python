grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}


def formatted_grades(students):
    string_list = []
    count = 1
    for key, value in students.items():
        string_list.append('{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, grade[value]))
        count+=1
    return string_list


students = {'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'}

for el in formatted_grades(students):
    print(el)