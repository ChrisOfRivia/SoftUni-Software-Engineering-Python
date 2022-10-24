def find_miner_cords(matrix):
    for idx, group in enumerate(matrix):
        if 's' in group:
            result = [idx, group.index('s')]
            return result


cave = int(input())
route = input().split()

matrix = []

# * - a regular position on the field
# e - the end of the route
# c - coal
# s - miner

for i in range(cave):
    matrix.append([el for el in input().split()])

coal_counter = 0
over = False

for moves in route:
    rows, cols = find_miner_cords(matrix)

    if moves == 'up':
        if rows > 0:
            matrix[rows][cols] = '*'
            if matrix[rows - 1][cols] == 'c':
                coal_counter += 1
            elif matrix[rows - 1][cols] == 'e':
                print(f'Game over! ({rows - 1}, {cols})')
                over = True
                break
            matrix[rows - 1][cols] = 's'
        else:
            continue

    elif moves == 'right':
        if cols < len(matrix) - 1:
            matrix[rows][cols] = '*'
            if matrix[rows][cols + 1] == 'c':
                coal_counter += 1
            elif matrix[rows][cols + 1] == 'e':
                print(f'Game over! ({rows}, {cols + 1})')
                over = True
                break
            matrix[rows][cols + 1] = 's'
        else:
            continue

    elif moves == 'left':
        if cols > 0:
            matrix[rows][cols] = '*'
            if matrix[rows][cols - 1] == 'c':
                coal_counter += 1
            elif matrix[rows][cols - 1] == 'e':
                print(f'Game over! ({rows}, {cols - 1})')
                over = True
                break
            matrix[rows][cols - 1] = 's'
        else:
            continue

    elif moves == 'down':
        if rows < len(matrix) - 1:
            matrix[rows][cols] = '*'
            if matrix[rows + 1][cols] == 'c':
                coal_counter += 1
            elif matrix[rows + 1][cols] == 'e':
                print(f'Game over! ({rows + 1}, {cols})')
                over = True
                break
            matrix[rows + 1][cols] = 's'
        else:
            continue

if not over:
    missing_coal = 0

    for idx, group in enumerate(matrix):
        if 'c' in group:
            missing_coal += 1
    rows, cols = find_miner_cords(matrix)

    if missing_coal == 0:
        print(f"You collected all coal! ({rows}, {cols})")
    else:
        print(f"{missing_coal} pieces of coal left. ({rows}, {cols})")