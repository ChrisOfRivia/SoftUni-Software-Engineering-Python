from collections import deque

num_pumps = int(input())

stations = deque()
circles_for_one_start = deque()

for _ in range(num_pumps):
    petrol_and_distance_km = input()
    stations.append(petrol_and_distance_km)

starts = 0

while starts != num_pumps:
    tank = 0
    circles_for_one_start.append(0)
    first_pump = True
    for tries in stations:
        tries = tries.split(" ")
        petrol = int(tries[0])
        km = int(tries[1])
        if first_pump:
            tank += petrol

        if tank < km:
            while tank < km:
                tank += petrol
                circles_for_one_start[-1] += 1
        elif tank >= km and not first_pump:
            tank += petrol
            circles_for_one_start[-1] += 1

        first_pump = False

        tank -= km

    starts += 1
    stations.rotate(-1)

print(circles_for_one_start.index(min(circles_for_one_start)))

