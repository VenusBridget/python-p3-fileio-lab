def write_file(file_name, file_content):
    pass
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as write_file:
        write_file.write(file_content)

def append_file(file_name, append_content):
    pass
    with open(f'{file_name}.txt', mode='a', encoding='utf-8') as append_file:
        append_file.write(append_content)

def read_file(file_name):
    pass
    with open(f'{file_name}.txt', mode='r', encoding='utf-8') as read_file:
        return read_file.read()
