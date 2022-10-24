rows, cols = input().split(", ")

matrix = []
result = 0

for i in range(int(rows)):
    matrix.append([])
    line = input().split(", ")
    while len(matrix[i]) != int(cols):
        for num in line:
            matrix[i].append(int(num))
    result += sum(matrix[i])

print(result)
print(matrix)