race_route_size = int(input())
car_number = input()

race_route = []
car_row = 0
car_col = 0
tunnels = []
finish_row = 0
finish_col = 0
distance = 0
finish = False

for row in range(race_route_size):
    race_route.append(input().split())

for row in range(race_route_size):
    for col in range(race_route_size):

        if race_route[row][col] == "T":
            tunnels.append((row, col))

        if race_route[row][col] == "F":
            finish_row = row
            finish_col = col

command = input()

while command != "End":

    if command == "up":
        car_row -= 1

    if command == "down":
        car_row += 1

    if command == "left":
        car_col -= 1

    if command == "right":
        car_col += 1

    distance += 10

    if race_route[car_row][car_col] == "F":
        race_route[car_row][car_col] = "C"
        finish = True
        print(f"Racing car {car_number} finished the stage!")
        break

    if race_route[car_row][car_col] == "T":
        distance += 20

        tunnels.remove((car_row, car_col))
        race_route[car_row][car_col] = "."

        car_row, car_col = tunnels[0]
        race_route[car_row][car_col] = "."

    command = input()

if not finish:
    race_route[car_row][car_col] = "C"
    print(f"Racing car {car_number} DNF.")

print(f"Distance covered {distance} km.")

for row in race_route:
    print("".join(row))