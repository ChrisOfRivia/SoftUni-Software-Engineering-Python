from collections import deque

duration_of_green_light = int(input())
duration_of_free_window = int(input())

car_queue = deque()

current_seconds = 0

succesfully_passed = 0


crash = False

while True:
    command = input()
    if command == 'END':
        if not crash:
            print(f'Everyone is safe.')
            print(f'{succesfully_passed} total cars passed the crossroads.')
        break
    elif command == 'green':
        current_seconds = duration_of_green_light
        while current_seconds > 0 and car_queue:
            if len(car_queue[-1]) < current_seconds:
                first_car = car_queue.pop()
                current_seconds -= len(first_car)
                succesfully_passed += 1
            elif len(car_queue[-1]) <= current_seconds + duration_of_free_window:
                current_seconds = 0
                last_car = car_queue.pop()
                succesfully_passed += 1
            elif len(car_queue[-1]) > current_seconds + duration_of_free_window:
                crash = True
                crash_car = car_queue.pop()
                crash_place = crash_car[current_seconds + duration_of_free_window]
                print(f'A crash happened!')
                print(f'{crash_car} was hit at {crash_place}.')
                break
        if crash:
            break
    if crash:
        break
    else:
        car_queue.appendleft(command)

