def file_operations(path, additional_info, start_pos, count_chars):
    with open(path, 'a') as fh:
        fh.write(additional_info)
    with open(path, 'r') as fh:
        fh.seek(start_pos)
        read_line = fh.read(count_chars)
    return read_line