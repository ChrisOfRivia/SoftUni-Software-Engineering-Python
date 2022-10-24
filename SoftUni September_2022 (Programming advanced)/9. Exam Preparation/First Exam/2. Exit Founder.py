from collections import deque

players = deque(input().split(', '))

maze = []

for _ in range(6):
    maze.append(list(input().split()))

maze1 = maze[0]
maze2 = maze[1]
maze3 = maze[2]
maze4 = maze[3]
maze5 = maze[4]
maze6 = maze[5]

# •	Only one Exit - marked with the "E" letter
# •	Trap (one, many, or none) - marked with the "T" letter
# •	Wall (one, many, or none) - marked with the "W" letter
# •	Empty positions will be marked with "."

ignored_players = []

while True:

    current_player = players[0]
    cords = input().split(', ')
    pos_row = int(cords[0][-1])
    pos_col = int(cords[-1][0])
    if current_player in ignored_players:
        ignored_players.remove(current_player)
        players.rotate(1)
        continue

    if maze[pos_row][pos_col] == 'E':
        players.pop()
        print(f'{current_player} found the Exit and wins the game!')
        break

    elif maze[pos_row][pos_col] == 'T':
        players.popleft()
        print(f"{current_player} is out of the game! The winner is {players[0]}.")
        break

    elif maze[pos_row][pos_col] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        ignored_players.append(current_player)

    players.rotate(1)
