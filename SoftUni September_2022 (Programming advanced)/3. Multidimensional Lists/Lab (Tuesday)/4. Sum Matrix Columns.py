rows, cols = map(int, input().split(", "))

matrix = []

for i in range(rows):
    matrix.append([int(el) for el in input().split()])

result = 0
column = 0

for num_cols in range(cols):
    for num_row in range(rows):
        result += matrix[num_row][column]
    print(result)
    result = 0
    column += 1


