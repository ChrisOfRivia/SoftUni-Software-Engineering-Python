number_sequence = list(map(int, input().split(" ")))

removed_counter = 0
temp_number = 0

while number_sequence is not None:
    for i in range(len(number_sequence)):
        index = int(input())
        if index < 0:
            temp_number = number_sequence[0]
            removed_counter += temp_number
            last_number = number_sequence[-1]
            number_sequence.remove(number_sequence[0])
            number_sequence.insert(0, last_number)

        elif index > len(number_sequence) - 1:
            temp_number = number_sequence[-1]
            removed_counter += temp_number
            first_number = number_sequence[0]
            number_sequence.remove(number_sequence[-1])
            number_sequence.insert(0, first_number)

        else:
            temp_number = number_sequence[index]
            removed_counter += temp_number
            number_sequence.remove(number_sequence[index])

        for index_num, numbers in enumerate(number_sequence):
            if numbers <= temp_number:
                number_sequence[index_num] += temp_number
            elif numbers > temp_number:
                number_sequence[index_num] -= temp_number

    if not number_sequence:
        break
print(removed_counter)
