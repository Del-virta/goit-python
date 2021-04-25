import shutil

def create_archive(path, file_name, employee_residence):
    file_path = f'{path}/{file_name}'
    with open(file_path, 'wb') as fh:
        for key, value in employee_residence.items():
            fh.write(bytes(f'{key} {value}\n','utf-8'))
    
    archive_name = shutil.make_archive('backup', 'zip', path)
    return archive_name