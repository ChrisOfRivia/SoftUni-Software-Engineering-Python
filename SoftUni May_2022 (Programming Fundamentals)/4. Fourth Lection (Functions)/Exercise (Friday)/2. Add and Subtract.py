def sum_numbers(a, b):
    result = a + b
    return result


def subtract(result, c):
    subtraction = result - c
    return subtraction


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(subtract(sum_numbers(first_num, second_num), third_num))