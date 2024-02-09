text = input('Input text to charify: ')

charset = []
for t in text:
    char_t = ord(t)
    charset.append(char_t)

print(charset)
