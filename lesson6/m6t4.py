def navigate_clients(path, code):
    fh = open(path,'r')
    fh.seek(9)
    phrase = fh.readline()
    fh.close()
    return phrase