factor = int(input())
count = int(input())

list_of_nums = []

for nums in range(factor, factor * count + 1):
    if nums % factor == 0:
        list_of_nums.append(nums)
print(list_of_nums)