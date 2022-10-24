def length_is_valid(password):
    if 6 <= len(password) <= 10:
        return True
    else:
        print(f'Password must be between 6 and 10 characters')
        return False


def symbols_are_valid(password):
    all_symbols_valid = False
    for every_char in password:
        if every_char.isdigit() or every_char.isalpha():
            all_symbols_valid = True
        else:
            print(f'Password must consist only of letters and digits')
            return False
    if all_symbols_valid:
        return True


def have_at_least_two_digits(password):
    digits = 0
    for every_chars in password:
        if every_chars.isdigit():
            digits += 1
    if digits >= 2:
        return True
    else:
        print(f'Password must have at least 2 digits')
        return False


password_input = input()
validated = [length_is_valid(password_input),
             symbols_are_valid(password_input),
             have_at_least_two_digits(password_input)]

if all(validated):
    print(f'Password is valid')