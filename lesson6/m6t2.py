
import pathlib


def write_and_get_employees(employee_list, path):
    fh = open(path, 'w')
    for employees in employee_list:
        for employee in employees:
            fh.write(f'{employee}\n')
    fh.close()
    fh = open(path, 'r')
    new_employee_list = fh.readlines()
    fh.close()
    return new_employee_list
employee_list = [['Robert Stivenson, 28 years', 'Alex Denver, 30 years'],['Drake Mikelsson, 19 years']]
path = pathlib.Path('E:/test.txt')
print(write_and_get_employees(employee_list, path))