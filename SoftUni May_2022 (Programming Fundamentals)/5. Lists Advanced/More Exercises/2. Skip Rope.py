some_string = input()

other = []
result = []

numbers = []
take_numbers = []
skip_numbers = []

for each_symbol in some_string:
    if each_symbol.isdigit():
        each_symbol = int(each_symbol)
        numbers.append(each_symbol)
    else:
        other.append(each_symbol)

for index, each_num in enumerate(numbers):
    if index % 2 == 0:
        take_numbers.append(each_num)
    else:
        skip_numbers.append(each_num)

for takes, skips in zip(take_numbers, skip_numbers):
    for take_nums in other[:takes]:
        if takes != 0:
            result.append(take_nums)
            other.remove(take_nums)
            takes -= 1
    for skip_nums in other[:skips]:
        if skips != 0:
            other.remove(skip_nums)
            skips -= 1
    if takes == 0 and skips == 0:
        continue

print(*result, sep="")
