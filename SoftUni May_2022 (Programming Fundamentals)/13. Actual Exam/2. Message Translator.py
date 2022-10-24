import re

n = int(input())

regex = r'\!(?P<command>[A-Z][a-z]{2,})\!\:\[(?P<message>[A-Za-z]{8,})\]'

for commands in range(n):
    text = input()

    list_command = [item.groupdict() for item in re.finditer(regex, text)]

    if len(list_command) != 0:
        for items in list_command:
            list_ascii = [str(ord(word)) for word in items["message"]]
            print(f'{items["command"]}: {" ".join(list_ascii)}')
    else:
        print(f'The message is invalid')