from math import floor


def coordinate_system_nearest_point(x1, y1, x2, y2):
    if abs(x2) + abs(y2) > abs(x1) + abs(y1):
        return f'({floor(x1)}, {floor(y1)})'
    elif abs(x1) + abs(y1) > abs(x2) + abs(y2):
        return f'({floor(x2)}, {floor(y2)})'
    elif abs(x1) + abs(y1) == abs(x2) + abs(y2):
        return f'({floor(x1)}, {floor(y1)})'


first_num = float(input())
second_num = float(input())
third_num = float(input())
fourth_num = float(input())
print(coordinate_system_nearest_point(first_num, second_num, third_num, fourth_num))