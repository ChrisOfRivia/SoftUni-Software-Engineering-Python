chat = []

while True:
    command = input()
    if command == 'end':
        break
    else:
        split = command.split(" ")
        event = split[0]
        message = split[1]

    if event == 'Chat':
        chat.append(message)
    elif event == 'Delete':
        if message in chat:
            chat.remove(message)
        else:
            continue
    elif event == 'Edit':
        edited_message = split[2]
        if message in chat:
            index_message = chat.index(message)
            chat[index_message] = edited_message
        else:
            continue
    elif event == 'Pin':
        if message in chat:
            chat.remove(message)
            chat.append(message)
        else:
            continue
    elif event == 'Spam':
        for every_spam_message in split[1::]:
            chat.append(every_spam_message)
for messages in chat:
    '\n'.join(messages)
    print(messages)