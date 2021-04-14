files = ['script.py', 'document.doc', 'folder', 'bacup.tar.gz']

for file in files:
    try:
        #idx = file.find('.')
        idx = file.rindex('.')
    except ValueError:
        print(f'{file} has no suffix')
        continue

    suffix = file[idx+1:]
    print(file, suffix)