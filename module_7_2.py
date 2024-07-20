def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    string_positions = {}
    for line, string in enumerate(strings):
        byte_positions = file.tell()
        file.write(string + '\n')
        string_positions[(line, byte_positions)] = string
    file.close()
    return string_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!']

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
