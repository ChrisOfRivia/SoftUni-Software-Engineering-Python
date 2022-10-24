list_of_nums_start = [0, 0, 1]
list_of_nums_extend = [1]


def tribonacci_sequence(number):
    for i in range(1, number):
        sum_three_nums = list_of_nums_start[-3] + list_of_nums_start[-2] + list_of_nums_start[-1]
        list_of_nums_extend.append(sum_three_nums)
        list_of_nums_start.append(sum_three_nums)
    for nums in list_of_nums_extend:
        print(nums, end=" ")


num = int(input())
tribonacci_sequence(num)
