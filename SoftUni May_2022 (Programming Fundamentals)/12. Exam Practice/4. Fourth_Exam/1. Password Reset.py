predefined_string = input()

while True:
    command = input().split(' ')
    action = command[0]
    if action == 'Done':
        print(f'Your password is: {predefined_string}')
        break

    elif action == 'TakeOdd':
        predefined_string = [chars for i, chars in enumerate(predefined_string) if i % 2 != 0]
        predefined_string = ''.join(predefined_string)
        print(predefined_string)

    elif action == 'Cut':
        index_cut = int(command[1])
        length_cut = int(command[2])
        predefined_string = [ch for j, ch in enumerate(predefined_string) if j < index_cut or j >= index_cut + length_cut]
        predefined_string = ''.join(predefined_string)
        print(predefined_string)

    elif action == 'Substitute':
        substring = command[1]
        substitute = command[2]
        if substring in predefined_string:
            predefined_string = predefined_string.replace(substring, substitute)
            print(predefined_string)
        else:
            print('Nothing to replace!')
