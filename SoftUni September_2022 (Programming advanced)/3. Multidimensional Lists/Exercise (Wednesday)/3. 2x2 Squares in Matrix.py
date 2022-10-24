rows, cols = map(int, input().split(" "))

matrix = []

for row in range(rows):
    matrix.append([el for el in input().split()])

equal_cells = 0
for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
            equal_cells += 1

    print(equal_cells)

