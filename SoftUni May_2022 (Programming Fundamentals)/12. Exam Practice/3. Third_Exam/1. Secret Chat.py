concealed_message = input()

while True:
    command = input().split(':|:')
    action = command[0]
    if action == 'Reveal':
        print(f'You have a new text message: {concealed_message}')
        break
    elif action == 'InsertSpace':
        space_index = int(command[1])
        concealed_message = f'{concealed_message[:space_index:]} {concealed_message[space_index::]}'
        print(concealed_message)
    elif action == 'Reverse':
        substring = command[1]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, '', 1)
            concealed_message += substring[::-1]
            print(concealed_message)
        else:
            print('error')
    elif action == 'ChangeAll':
        substring = command[1]
        replacement = command[2]
        if substring in concealed_message:
            concealed_message = concealed_message.replace(substring, replacement)
            print(concealed_message)


