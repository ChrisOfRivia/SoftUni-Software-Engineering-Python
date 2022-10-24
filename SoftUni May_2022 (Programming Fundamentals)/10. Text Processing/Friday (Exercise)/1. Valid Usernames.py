usernames = input().split(', ')

for each_user in usernames:
    valid_1 = False
    valid_2 = False
    if 3 <= len(each_user) <= 16:
        valid_1 = True
    else:
        continue

    for char in each_user:
        redundant_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '=', '+', '[', ']', '{', '}', '/', ' ']
        if char in redundant_symbols:
            valid_2 = False
            break
        elif char.isalpha or char.isnumeric or char == '-' or char == '_':
            valid_2 = True
        else:
            continue
    if not valid_2:
        continue

    if valid_1 and valid_2:
        print(each_user)
