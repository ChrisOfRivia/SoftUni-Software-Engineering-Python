numbers = input().split(" ")

list_of_nums = []

for num in numbers:
    num = int(num)
    num *= -1
    list_of_nums.append(int(num))
print(list_of_nums)