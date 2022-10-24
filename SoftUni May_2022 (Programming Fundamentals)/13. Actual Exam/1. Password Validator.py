import string

password = input()
num_uppers = 0
num_lowers = 0
num_digits = 0

while True:
    command = input().split(' ')
    action = command[0]
    if action == 'Complete':
        break

    elif action == 'Make':
        if command[1] == 'Upper':
            index_upper = int(command[2])
            password = f'{password[:index_upper]}{password[index_upper].upper()}{password[index_upper + 1 ::]}'
            print(password)
        elif command[1] == 'Lower':
            index_lower = int(command[2])
            password = f'{password[:index_lower]}{password[index_lower].lower()}{password[index_lower + 1::]}'
            print(password)

    elif action == 'Insert':
        index_insert = int(command[1])
        char_insert = command[2]
        if index_insert < len(password):
            password = f'{password[:index_insert:]}{char_insert}{password[index_insert::]}'
            print(password)
        else:
            continue

    elif action == 'Replace':
        char_replace = command[1]
        value = int(command[2])
        ascii_value = ord(char_replace)
        ascii_value += value
        if char_replace in password:
            password = password.replace(char_replace, chr(ascii_value))
            print(password)
        else:
            pass
    elif action == 'Validation':
        num_uppers = 0
        num_lowers = 0
        num_digits = 0

        if len(password) < 8:
            print(f'Password must be at least 8 characters long!')

        for char_symbols in password:
            if char_symbols not in string.ascii_letters and char_symbols not in string.digits and char_symbols != '_':
                print(f'Password must consist only of letters, digits and _!')
                break

        for char_upper in password:
            if char_upper in string.ascii_uppercase:
                num_uppers += 1
        if num_uppers == 0:
            print(f'Password must consist at least one uppercase letter!')

        for char_lower in password:
            if char_lower in string.ascii_lowercase:
                num_lowers += 1
        if num_lowers == 0:
            print(f'Password must consist at least one lowercase letter!')

        for char_digit in password:
            if char_digit in string.digits:
                num_digits += 1
        if num_digits == 0:
            print(f'Password must consist at least one digit!')
