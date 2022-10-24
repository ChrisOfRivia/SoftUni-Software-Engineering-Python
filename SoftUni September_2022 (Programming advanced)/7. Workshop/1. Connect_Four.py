def connect_four_start(word):
    if word.upper() == 'Y':
        print('\nStarting game... ')
        connect_four_board = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
        ]
        for rows in connect_four_board:
            print(rows)
        return connect_four_board

    elif word.upper() == 'Q' or word.upper() == 'N':
        print('\nQuitting game... ')
        exit()


def place_symbol(board, column, player):
    counter = 0
    available_last_row = 0
    for num in range(1, 7):
        if board[-num][column] != 0:
            pass
        elif board[-num][column] == 0:
            available_last_row = -num
            break

    if counter == 0:
        print()
        counter += 1

    if player == 'Player 1':
        board[available_last_row][column] = 1
        for groups in board:
            print(groups)

    elif player == 'Player 2':
        board[available_last_row][column] = 2
        for groups in board:
            print(groups)


while True:
    board = connect_four_start(input('\nWelcome to Connect Four! Would you like to start the game? (Y/N): '))
    if not board:
        continue
    else:
        break

connected_four = False
player = ''

while not connected_four:
    command = input('\nPlayer 1, select a column to place: (Q-Quit)|(R-Restart) ')
    player = 'Player 1'

    if command.upper() == 'R':
        reassurement = input('\nAre you sure? (Y/N): ')
        if reassurement.upper() == 'Y':
            print('\nRestarting game...')
            board = connect_four_start(input('\nWelcome to Connect Four! Would you like to start the game? (Y/N): '))
        elif reassurement.upper() == 'N':
            continue

    elif command.upper() == 'Q':
        print('\nQuitting game... ')
        exit()

    elif command.isnumeric():
        command = int(command)

        while command >= 7:
            command = input('\nColumn is out of range, please pick a number between 0 and 6: ')
            command = int(command)

        result = place_symbol(board, command, player)
        if result == '':
            pass

    command = input('\nPlayer 2, select a column to place: (Q-Quit)|(R-Restart) ')
    player = 'Player 2'

    if command.upper() == 'R':
        reassurement = input('\nAre you sure? (Y/N): ')
        if reassurement.upper() == 'Y':
            print('\nRestarting game...')
            board = connect_four_start(input('\nWelcome to Connect Four! Would you like to start the game? (Y/N): '))
        elif reassurement.upper() == 'N':
            continue

    elif command.upper() == 'Q':
        print('\nQuitting game... ')
        exit()

    elif command.isnumeric():
        command = int(command)

        while command >= 7:
            command = input('\nColumn is out of range, please pick a number between 0 and 6: ')
            command = int(command)

        result = place_symbol(board, command, player)
        if result == '':
            pass
