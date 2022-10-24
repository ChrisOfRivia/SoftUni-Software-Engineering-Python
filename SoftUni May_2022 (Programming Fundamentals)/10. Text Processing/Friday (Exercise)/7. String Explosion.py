string = input()

new_str = ''
previous_char = ''
explosion = 0

for i, char in enumerate(string):
    if i == 0:
        previous_char = char
        new_str += char
    else:
        if previous_char == '>':
            previous_char = char
            explosion += int(char)
            explosion -= 1
            continue
        if explosion > 0 and char != '>':
            explosion -= 1
            continue

        else:
            new_str += char
            previous_char = char

print(new_str)