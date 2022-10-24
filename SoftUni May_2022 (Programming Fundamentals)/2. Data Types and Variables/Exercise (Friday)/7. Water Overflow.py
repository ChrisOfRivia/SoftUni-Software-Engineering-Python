pouring_times = int(input())

tank = 0
max_tank = 255

for each_time in range(pouring_times):
    water = int(input())
    if tank + water > max_tank:
        print("Insufficient capacity!")
        continue
    else:
        tank += water
print(tank)