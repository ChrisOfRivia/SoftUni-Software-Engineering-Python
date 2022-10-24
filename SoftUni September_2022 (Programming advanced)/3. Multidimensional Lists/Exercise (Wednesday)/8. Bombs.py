def get_children(matrix, row, col):
    possible_children = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]

    result = []

    for child_row, child_col in possible_children:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


n = int(input())
matrix = []

for i in range(n):
    matrix.append([int(el) for el in input().split()])

bombs = input().split()

for bomb in bombs:
    rows, cols = [int(x) for x in bomb.split(',')]
    bomb_power = matrix[rows][cols]
    if bomb_power <= 0:
        continue

    children = get_children(matrix, rows, cols)
    for victims in children:
        first_num = victims[0]
        second_num = victims[1]

        matrix[first_num][second_num] -= bomb_power
    matrix[rows][cols] = 0

alive_cells = [el for sublist in matrix for el in sublist if el > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for cells in matrix:
    print(' '.join(map(str, cells)))
                  