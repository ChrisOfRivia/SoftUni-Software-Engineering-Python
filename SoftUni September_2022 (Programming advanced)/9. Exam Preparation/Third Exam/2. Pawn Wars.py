chess_table = []

while len(chess_table) != 8:
    chess_table.append(input().split())

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
path = [8, 7, 6, 5, 4, 3, 2, 1]

row_8 = chess_table[0]
row_7 = chess_table[1]
row_6 = chess_table[2]
row_5 = chess_table[3]
row_4 = chess_table[4]
row_3 = chess_table[5]
row_2 = chess_table[6]
row_1 = chess_table[7]

white_cords = ''
black_cords = ''

for idx_cols, cols in enumerate(chess_table):
    for idx_chr, chr in enumerate(cols):
        if chr == 'w':
            white_cords = idx_cols, idx_chr
        elif chr == 'b':
            black_cords = idx_cols, idx_chr

white_row = int(white_cords[0])
white_col = int(white_cords[1])

black_row = int(black_cords[0])
black_col = int(black_cords[1])

while True:
    if white_col > 0:
        if chess_table[white_row - 1][white_col - 1] == 'b':
            chess_table[white_row - 1][white_col - 1] = 'w'
            chess_table[white_row][white_col] = '-'
            white_row -= 1
            white_col -= 1

            print(f"Game over! White win, capture on {columns[white_col]}{path[white_row]}.")
            break
    if white_col < 7:
        if chess_table[white_row - 1][white_col + 1] == 'b':
            chess_table[white_row - 1][white_col + 1] = 'w'
            chess_table[white_row][white_col] = '-'
            white_row -= 1
            white_col += 1

            print(f"Game over! White win, capture on {columns[white_col]}{path[white_row]}.")
            break

    chess_table[white_row - 1][white_col] = 'w'
    chess_table[white_row][white_col] = '-'
    white_row -= 1

    if white_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {columns[white_col]}{path[white_row]}.")
        break

    if black_col > 0:
        if chess_table[black_row + 1][black_col - 1] == 'w':
            chess_table[black_row + 1][black_col - 1] = 'b'
            chess_table[black_row][black_col] = '-'
            black_row += 1
            black_col -= 1

            print(f"Game over! Black win, capture on {columns[black_col]}{path[black_row]}.")
            break

    if black_col < 7:
        if chess_table[black_row + 1][black_col + 1] == 'w':
            chess_table[black_row + 1][black_col + 1] = 'b'
            chess_table[black_row][black_col] = '-'
            black_row += 1
            black_col += 1

            print(f"Game over! Black win, capture on {columns[black_col]}{path[black_row]}.")
            break

    chess_table[black_row + 1][black_col] = 'b'
    chess_table[black_row][black_col] = '-'
    black_row += 1

    if black_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {columns[black_col]}{path[black_row]}.")
        break
