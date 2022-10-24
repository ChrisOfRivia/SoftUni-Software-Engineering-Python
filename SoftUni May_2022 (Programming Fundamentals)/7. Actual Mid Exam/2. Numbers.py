number_sequence = list(map(int, input().split(" ")))

while True:
    command = input()
    if command == 'Finish':
        break
    else:
        split = command.split(" ")
        event = split[0]
        number = int(split[1])
    if event == 'Add':
        number_sequence.append(number)
    elif event == 'Remove':
        if number in number_sequence:
            number_sequence.remove(number)
    elif event == 'Replace':
        replace_num = int(split[2])
        if number in number_sequence:
            num_index = number_sequence.index(number)
            number_sequence[num_index] = replace_num
    elif event == 'Collapse':
        for nums in reversed(number_sequence):
            if nums < number:
                number_sequence.remove(nums)
print(*number_sequence, sep=" ")