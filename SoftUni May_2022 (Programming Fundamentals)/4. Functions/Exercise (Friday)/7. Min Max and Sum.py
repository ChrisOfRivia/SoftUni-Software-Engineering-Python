def min_num(nums):
    for num in nums:
        list_for_min.append(num)
    return min(list_for_min)


def max_num(nums):
    for num in nums:
        list_for_max.append(num)
    return max(list_for_max)


def sum_nums(nums):
    for num in nums:
        list_for_sum.append(num)
    return sum(list_for_max)


list_for_min = []
list_for_max = []
list_for_sum = []
numbers = list(map(int, input().split(" ")))
print(f'The minimum number is {min_num(numbers)}')
print(f'The maximum number is {max_num(numbers)}')
print(f'The sum number is: {sum_nums(numbers)}')

