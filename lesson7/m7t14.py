def to_indexed(start_file, end_file):
    with open(start_file, 'r') as fh:
        start_file_lines = fh.readlines()
    new_string = ''
    with open(end_file,'w') as fh:
        for i in range(len(start_file_lines)):
            new_string = f'{i}: {start_file_lines[i]}'
            fh.write(new_string)