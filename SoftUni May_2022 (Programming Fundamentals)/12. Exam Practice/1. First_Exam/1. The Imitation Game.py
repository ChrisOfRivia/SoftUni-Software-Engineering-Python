message = input()
list_of_chars = []

for char in message:
    list_of_chars.append(char)

while True:
    command = input()
    if command == 'Decode':
        break
    else:
        command = command.split("|")
        action = command[0]

    if action == 'Move':
        num = int(command[1])
        while num != 0:
            list_of_chars.append(list_of_chars[0])
            list_of_chars.remove(list_of_chars[0])
            num -= 1

    elif action == 'Insert':
        index = int(command[1])
        value = command[2]
        if len(value) == 1:
            list_of_chars.insert(index, value)
        else:
            for i, letter in enumerate(value):
                list_of_chars.insert(index + i, letter)

    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        while substring in list_of_chars:
            index_of_substring = list_of_chars.index(substring)
            list_of_chars[index_of_substring] = replacement

print(f'The decrypted message is: {"".join(list_of_chars)}')