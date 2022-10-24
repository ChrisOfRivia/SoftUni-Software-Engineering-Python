text = input()

previous_char = ""

for i, char in enumerate(text):
    if i == 0:
        previous_char = char
    else:
        if previous_char == ':':
            print(f':{char}')
        previous_char = char