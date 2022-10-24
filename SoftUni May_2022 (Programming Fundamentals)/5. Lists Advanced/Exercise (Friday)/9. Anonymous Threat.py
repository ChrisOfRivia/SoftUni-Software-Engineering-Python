commands = input().split(" ")
new_commands = ''
merged_string = ''
divided_string = ''

while True:
    new_commands = input()
    if new_commands == '3:1':
        break
    new_commands = new_commands.split(" ")
    action = new_commands[0]
    start_index = int(new_commands[1])
    end_index = int(new_commands[2])
    if start_index < 0:
        start_index = 0
    if action == 'merge':
        merged_string = ''
        if end_index > len(commands):
            merged_string += ''.join(commands[start_index::])
            for word in commands[start_index::]:
                commands.remove(word)
            commands.insert(start_index, merged_string)
        else:
            merged_string += ''.join(commands[start_index:end_index + 1:])
            for word in commands[start_index:end_index + 1:]:
                commands.remove(word)
            commands.insert(start_index, merged_string)
    elif action == 'divide':
        for string in merged_string:
            split_equally = len(merged_string) // end_index
            if merged_string in commands:
                commands.remove(merged_string)
            divided_string += string
            if len(divided_string) == split_equally:
                commands.append(divided_string)
                divided_string = ''
            elif len(divided_string) > split_equally:
                commands.append(divided_string)
                divided_string = ''

if " " in commands:
    commands.remove(" ")

print(*commands)
