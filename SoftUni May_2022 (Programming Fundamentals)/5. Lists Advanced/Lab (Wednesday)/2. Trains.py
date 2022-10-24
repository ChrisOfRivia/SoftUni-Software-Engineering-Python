command = ''
counter = 0
wagon_size = int(input())
train = [0] * wagon_size


while True:
    command = input()
    if command == 'End':
        break
    counter += 1
    split_command = command.split(" ")
    event = split_command[0]
    number_index = int(split_command[1])
    if len(split_command) > 2:
        number_people = split_command[2]

    if event == 'add':
        train[-1] = train[-1] + number_index
    elif event == 'insert':
        train[number_index] = train[number_index] + int(split_command[2])
    elif event == 'leave':
        train[number_index] = train[number_index] - int(split_command[2])

print(train)


