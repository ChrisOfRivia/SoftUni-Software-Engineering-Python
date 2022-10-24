def bunny_moves(matrix, bunny_cords):
    moves = {'up': [], 'right': [], 'left': [], 'down': []}

    while True:
        row_cord = bunny_cords[0]
        col_cord = bunny_cords[1]
        for moves_up in range(len(matrix)):
            if 0 < row_cord:
                if matrix[row_cord - 1][col_cord] != 'X':
                    moves['up'].append([row_cord - 1, col_cord])
                    row_cord -= 1
                else:
                    break
            else:
                break

        if len(moves['up']) == 0:
            moves.pop('up')

        row_cord = bunny_cords[0]
        col_cord = bunny_cords[1]

        for moves_right in range(len(matrix)):
            if col_cord < len(matrix) - 1:
                if matrix[row_cord][col_cord + 1] != 'X':
                    moves['right'].append([row_cord, col_cord + 1])
                    col_cord += 1
                else:
                    break
            else:
                break

        if len(moves['right']) == 0:
            moves.pop('right')

        row_cord = bunny_cords[0]
        col_cord = bunny_cords[1]

        for moves_left in range(len(matrix)):
            if 0 < col_cord:
                if matrix[row_cord][col_cord - 1] != 'X':
                    moves['left'].append([row_cord, col_cord - 1])
                    col_cord -= 1
                else:
                    break
            else:
                break

        if len(moves['left']) == 0:
            moves.pop('left')

        row_cord = bunny_cords[0]
        col_cord = bunny_cords[1]

        for moves_down in range(len(matrix)):
            if row_cord < len(matrix) - 1:
                if matrix[row_cord + 1][col_cord] != 'X':
                    moves['down'].append([row_cord + 1, col_cord])
                    row_cord += 1
                else:
                    break
            else:
                break

        if len(moves['down']) == 0:
            moves.pop('down')

        return moves


size_of_field = int(input())

matrix = []

for rows in range(size_of_field):
    matrix.append([el for el in input().split()])

bunny_cords = []

for idx_row, group in enumerate(matrix):
    for idx_col, ch in enumerate(group):
        if ch == 'B':
            bunny_cords = [idx_row, idx_col]
            break

possible_ways_to_go = bunny_moves(matrix, bunny_cords)

max_direction = ''
max_sum = 0
first_try = True

for every_way, cords in possible_ways_to_go.items():
    max_sum_of_one_way = 0
    for every_cord in cords:
        row_num = every_cord[0]
        col_num = every_cord[1]
        max_sum_of_one_way += int(matrix[row_num][col_num])

    if first_try:
        max_direction = every_way
        max_sum = max_sum_of_one_way
        first_try = False

    else:
        if max_sum_of_one_way > max_sum:
            max_sum = max_sum_of_one_way
            max_direction = every_way

print(max_direction)
for every_direction in possible_ways_to_go[max_direction]:
    print(every_direction)
print(max_sum)