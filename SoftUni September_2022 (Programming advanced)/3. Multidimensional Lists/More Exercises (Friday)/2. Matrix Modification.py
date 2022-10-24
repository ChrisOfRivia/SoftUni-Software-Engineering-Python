size = int(input())

matrix = []

for i in range(size):
    matrix.append([el for el in map(int, input().split())])

while True:
    command = input().split()
    if command[0] == 'END':
        break

    elif command[0] == 'Add':
        first_cord = int(command[1])
        second_cord = int(command[2])
        number = int(command[3])
        if 0 <= first_cord < (len(matrix)) and 0 <= second_cord < (len(matrix)):
            matrix[first_cord][second_cord] += number
        else:
            print("Invalid coordinates")
            continue

    elif command[0] == 'Subtract':
        first_cord = int(command[1])
        second_cord = int(command[2])
        number = int(command[3])
        if 0 <= first_cord < (len(matrix)) and 0 <= second_cord < (len(matrix)):
            matrix[first_cord][second_cord] -= number
        else:
            print("Invalid coordinates")
            continue

for groups in matrix:
    print(*groups)