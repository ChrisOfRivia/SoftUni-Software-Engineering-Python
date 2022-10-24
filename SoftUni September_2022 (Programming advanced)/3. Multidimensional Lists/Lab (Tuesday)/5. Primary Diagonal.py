n = int(input())

matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split(" ")])

num_queue = 0
result = 0

for each_column in matrix:
    result += each_column[num_queue]
    num_queue += 1

print(result)