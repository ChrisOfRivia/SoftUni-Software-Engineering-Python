rows = int(input())

matrix = []

for i in range(rows):
    matrix.append([])
    nums = [int(el) for el in input().split(", ")]
    even_nums = [el for el in nums if el % 2 == 0]
    for nums in even_nums:
        matrix[i].append(nums)

print(matrix)