def str_to_binary(text):
    binary_list = []
    for char in text:
        binary_list.append(format(ord(char), '08b'))
        binary_list.append(' ')
    return ''.join(binary_list)

text = input('Text to convert: ')
converted = str_to_binary(text)

print(converted)
