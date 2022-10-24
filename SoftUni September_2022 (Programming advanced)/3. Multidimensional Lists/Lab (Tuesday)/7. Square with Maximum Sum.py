rows, cols = map(int, input().split(", "))

matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split(", ")])

"""
    7 1 3 3 2 1
    1 3 9 8 5 6
    4 6 7 9 1 0
"""

groups = -1
max_sum = [0]

for groups in range(rows - 1):
    for num in range(cols - 1):
        if matrix[groups][num] + matrix[groups][num + 1] + matrix[groups + 1][num] + matrix[groups + 1][num + 1] > sum(max_sum):
            max_sum = [matrix[groups][num], matrix[groups][num + 1],
                       matrix[groups + 1][num], matrix[groups + 1][num + 1]]

print(max_sum[0], max_sum[1])
print(max_sum[2], max_sum[3])
print(sum(max_sum))
