num_letter_groups = input().split()

uppercase_alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]

lowercase_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z']

current_num = 0

all_nums = []

for each_num_letter in num_letter_groups:
    first_letter = each_num_letter[0]
    second_letter = each_num_letter[-1]
    nums_between = int(each_num_letter[1:-1])
    current_num = 0

    if first_letter.isupper():
        current_num += nums_between / (uppercase_alpha.index(first_letter) + 1)
    elif first_letter.islower():
        current_num += nums_between * (lowercase_alpha.index(first_letter) + 1)

    if second_letter.isupper():
        current_num -= (uppercase_alpha.index(second_letter) + 1)
    elif second_letter.islower():
        current_num += (lowercase_alpha.index(second_letter) + 1)

    all_nums.append(current_num)

print(f'{sum(all_nums):.2f}')

