def check_positions(table, row, col, command, direction, value=''):
    if direction == 'up':
        if row > 0:
            if command == 'Create':
                if table[row - 1][col] == '.':
                    table[row - 1][col] = value

            elif command == 'Update':
                if table[row - 1][col] != '.':
                    table[row - 1][col] = value

            elif command == 'Delete':
                if table[row - 1][col] != '.':
                    table[row - 1][col] = '.'

            elif command == 'Read':
                if table[row - 1][col] != '.':
                    print(table[row - 1][col])

            return row - 1, col
        else:
            return ()

    elif direction == 'down':
        if row < 5:
            if command == 'Create':
                if table[row + 1][col] == '.':
                    table[row + 1][col] = value

            elif command == 'Update':
                if table[row + 1][col] != '.':
                    table[row + 1][col] = value

            elif command == 'Delete':
                if table[row + 1][col] != '.':
                    table[row + 1][col] = '.'

            elif command == 'Read':
                if table[row + 1][col] != '.':
                    print(table[row + 1][col])

            return row + 1, col
        else:
            return ()

    elif direction == 'left':
        if col > 0:
            if command == 'Create':
                if table[row][col - 1] == '.':
                    table[row][col - 1] = value

            elif command == 'Update':
                if table[row][col - 1] != '.':
                    table[row][col - 1] = value

            elif command == 'Delete':
                if table[row][col - 1] != '.':
                    table[row][col - 1] = '.'

            elif command == 'Read':
                if table[row][col - 1] != '.':
                    print(table[row][col - 1])

            return row, col - 1

        else:
            return ()

    elif direction == 'right':
        if col < 5:
            if command == 'Create':
                if table[row][col + 1] == '.':
                    table[row][col + 1] = value

            elif command == 'Update':
                if table[row][col + 1] != '.':
                    table[row][col + 1] = value

            elif command == 'Delete':
                if table[row][col + 1] != '.':
                    table[row][col + 1] = '.'

            elif command == 'Read':
                if table[row][col + 1] != '.':
                    print(table[row][col + 1])

            return row, col + 1

        else:
            return ()


table = []

while len(table) != 6:
    table.append([str(el) for el in list(input().split())])

row1 = table[0]
row2 = table[1]
row3 = table[2]
row4 = table[3]
row5 = table[4]
row6 = table[5]

position = input().split(', ')
pos_row = int(position[0][-1])
pos_col = int(position[1][0])
direction = ''

while True:
    command = input().split(', ')
    if command[0] == 'Stop':
        break

    if command[0] == 'Create':
        direction_create = command[1]
        value_create = command[2]
        new_positions = check_positions(table, pos_row, pos_col, command[0], direction_create, value_create)
        if new_positions:
            pos_row = new_positions[0]
            pos_col = new_positions[1]

    elif command[0] == 'Update':
        direction_update = command[1]
        value_update = command[2]
        new_positions = check_positions(table, pos_row, pos_col, command[0], direction_update, value_update)
        if new_positions:
            pos_row = new_positions[0]
            pos_col = new_positions[1]

    elif command[0] == 'Delete':
        direction_delete = command[1]
        new_positions = check_positions(table, pos_row, pos_col, command[0], direction_delete)
        if new_positions:
            pos_row = new_positions[0]
            pos_col = new_positions[1]

    elif command[0] == 'Read':
        direction_read = command[1]
        new_positions = check_positions(table, pos_row, pos_col, command[0], direction_read)
        if new_positions:
            pos_row = new_positions[0]
            pos_col = new_positions[1]

for rows in table:
    print(' '.join(rows))