num_matrix = int(input())

matrix = []

for i in range(num_matrix):
    nums = [int(el) for el in input().split(", ")]
    matrix.append(nums)

print([el for i in range(num_matrix) for el in matrix[i]])
