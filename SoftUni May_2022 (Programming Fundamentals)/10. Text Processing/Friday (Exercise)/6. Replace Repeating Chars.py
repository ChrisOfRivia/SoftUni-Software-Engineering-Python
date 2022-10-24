previous_char = ''
fixed_text = ''

long_text = input()

for i, char in enumerate(long_text):
    if i == 0:
        fixed_text += char
        previous_char = char
    else:
        if char == previous_char:
            continue
        else:
            previous_char = char
            fixed_text += char

print(fixed_text)