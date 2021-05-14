def get_employees_by_profession(path, profession):
    with open(path, 'r') as fh:
        file_lines = fh.readlines()
    prof_list = []
    for each_line in file_lines:
        if each_line.find(profession) != (-1):
            prof_list.append(each_line)
    prof_string = ' '.join(prof_list).replace(' '+profession, '')
    return prof_string.replace('\n', '')
