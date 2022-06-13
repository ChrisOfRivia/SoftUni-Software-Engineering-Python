from math import floor

#
# def original_nums(a, b, number):
#     if (abs(a) + abs(b)) == number:
#         return int(a), int(b)
#     else:
#         return -1
#
#
# def max_pair(x1, y1, x2, y2, x3, y3, x4, y4):
#     first_pair = abs(x1) + abs(y1)
#     second_pair = abs(x2) + abs(y2)
#     third_pair = abs(x3) + abs(y3)
#     fourth_pair = abs(x4) + abs(y4)
#     list_nums = list((first_pair, second_pair, third_pair, fourth_pair))
#     return list_nums
#
#
def coordinate_system_longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    larger_numbers = 0
    second_largest_number = 0

    final_number_first = ''
    final_number_second = ''
    equal_length = False
#
#     list_nums = max_pair(x1, y1, x2, y2, x3, y3, x4, y4)
#     largest_number = max(list_nums)
#     list_nums.remove(largest_number)
#
#     second_largest_num = max(list_nums)
#
#     if original_nums(x1, y1, largest_number) != -1:
#         larger_numbers = original_nums(x1, y1, largest_number)
#
#     elif original_nums(x2, y2, largest_number) != -1:
#         larger_numbers = original_nums(x2, y2, largest_number)
#
#     elif original_nums(x3, y3, largest_number) != -1:
#         larger_numbers = original_nums(x3, y3, largest_number)
#
#     elif original_nums(x4, y4, largest_number) != -1:
#         larger_numbers = original_nums(x4, y4, largest_number)
#
#
#
#
#     if original_nums(x1, y1, second_largest_num) != -1:
#         second_largest_number = original_nums(x1, y1, second_largest_num)
#
#     elif original_nums(x2, y2, second_largest_num) != -1:
#         second_largest_number = original_nums(x2, y2, second_largest_num)
#
#     elif original_nums(x3, y3, second_largest_num) != -1:
#         second_largest_number = original_nums(x3, y3, second_largest_num)
#
#     elif original_nums(x4, y4, second_largest_num) != -1:
#         second_largest_number = original_nums(x4, y4, second_largest_num)
#
#     if second_largest_number == larger_numbers:
#         return second_largest_number
#     else:
#         return f'{second_largest_number}{larger_numbers}'

    # If the first pairs are the highest numbers
    if abs(x1) + abs(y1) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
        final_number_second = f'({floor(x1)}, {floor(y1)})'
        # If the second pairs are the second highest of the remaining 3 pairs
        if abs(x2) + abs(y2) == max((abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x2)}, {floor(y2)})'
            if abs(x1) + abs(y1) == abs(x2) + abs(y2):
                equal_length = True

        # If the third pairs are the second highest of the remaining 3 pairs
        elif abs(x3) + abs(y3) == max((abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x3)}, {floor(y3)})'
            if abs(x1) + abs(y1) == abs(x3) + abs(y3):
                equal_length = True

        # if the fourth pairs are the second highest of the remaining 3 pairs
        elif abs(x4) + abs(y4) == max((abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x4)}, {floor(y4)})'
            if abs(x1) + abs(y1) == abs(x4) + abs(y4):
                equal_length = True

    # If the second pairs are the highest numbers
    elif abs(x2) + abs(y2) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
        final_number_second = f'({floor(x2)}, {floor(y2)})'

        # If the first pairs are the second highest of the remaining 3 pairs
        if abs(x1) + abs(y1) == max((abs(x1) + abs(y1)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x1)}, {floor(y1)})'
            if abs(x2) + abs(y2) == abs(x1) + abs(y1):
                equal_length = True

        # If the third pairs are the second highest of the remaining 3 pairs
        elif abs(x3) + abs(y3) == max((abs(x1) + abs(y1)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x3)}, {floor(y3)})'
            if abs(x2) + abs(y2) == abs(x3) + abs(y3):
                equal_length = True

        # If the fourth pairs are the second highest of the remaining 3 pairs
        elif abs(x4) + abs(y4) == max((abs(x1) + abs(y1)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x4)}, {floor(y4)})'
            if abs(x2) + abs(y2) == abs(x4) + abs(y4):
                equal_length = True

    # If the third pairs are the highest numbers
    elif abs(x3) + abs(y3) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
        final_number_second = f'({floor(x3)}, {floor(y3)})'

        # If the first pairs are the second highest of the remaining 3 pairs
        if abs(x1) + abs(y1) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x1)}, {floor(y1)})'
            if abs(x3) + abs(y3) == abs(x1) + abs(y1):
                equal_length = True

        # If the second pairs are the second highest of the remaining 3 pairs
        elif abs(x2) + abs(y2) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x2)}, {floor(y2)})'
            if abs(x3) + abs(y3) == abs(x2) + abs(y2):
                equal_length = True

        # If the fourth pairs are the second highest of the remaining 3 pairs
        elif abs(x4) + abs(y4) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x4) + abs(y4))):
            final_number_first = f'({floor(x4)}, {floor(y4)})'
            if abs(x3) + abs(y3) == abs(x4) + abs(y4):
                equal_length = True

    # If the fourth pairs are the highest numbers
    elif abs(x4) + abs(y4) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3)), (abs(x4) + abs(y4))):
        final_number_second = f'({floor(x4)}, {floor(y4)})'

        # If the first pairs are the second highest of the remaining 3 pairs
        if abs(x1) + abs(y1) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3))):
            final_number_first = f'({floor(x1)}, {floor(y1)})'
            if abs(x4) + abs(y4) == abs(x1) + abs(y1):
                equal_length = True

        # If the second pairs are the second highest of the remaining 3 pairs
        elif abs(x2) + abs(y2) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3))):
            final_number_first = f'({floor(x2)}, {floor(y2)})'
            if abs(x4) + abs(y4) == abs(x2) + abs(y2):
                equal_length = True

        # If the third pairs are the second highest of the remaining 3 pairs
        elif abs(x3) + abs(y3) == max((abs(x1) + abs(y1)), (abs(x2) + abs(y2)), (abs(x3) + abs(y3))):
            final_number_first = f'({floor(x3)}, {floor(y3)})'
            if abs(x4) + abs(y4) == abs(x3) + abs(y3):
                equal_length = True
    if not equal_length:
        return f'{final_number_first}{final_number_second}'
    else:
        return f'{final_number_first}'


num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
num5 = float(input())
num6 = float(input())
num7 = float(input())
num8 = float(input())
print(coordinate_system_longer_line(num1, num2, num3, num4, num5, num6, num7, num8))
