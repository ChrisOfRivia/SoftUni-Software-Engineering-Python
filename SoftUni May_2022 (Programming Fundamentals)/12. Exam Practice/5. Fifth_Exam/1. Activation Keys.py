raw_activation_key = input()

raw_activation_key_list = []

while True:
    command = input().split('>>>')
    action = command[0]
    if action == 'Generate':
        print(f'Your activation key is: {raw_activation_key}')
        break

    elif action == 'Contains':
        substring = command[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif action == 'Flip':
        if command[1] == 'Upper':
            start_index_upper = int(command[2])
            end_index_upper = int(command[3])
            raw_activation_key = f'{raw_activation_key[:start_index_upper]}{raw_activation_key[start_index_upper:end_index_upper].upper()}{raw_activation_key[end_index_upper::]}'
            print(raw_activation_key)
        elif command[1] == 'Lower':
            start_index_lower = int(command[2])
            end_index_lower = int(command[3])
            raw_activation_key = f'{raw_activation_key[:start_index_lower]}{raw_activation_key[start_index_lower:end_index_lower:].lower()}{raw_activation_key[end_index_lower::]}'
            print(raw_activation_key)
    elif action == 'Slice':
        start_index_slice = int(command[1])
        end_index_slice = int(command[2])
        raw_activation_key = f'{raw_activation_key[:start_index_slice]}{raw_activation_key[end_index_slice::]}'
        print(raw_activation_key)
