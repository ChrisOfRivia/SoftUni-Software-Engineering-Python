n = int(input())

initial_car_dict = {}

for i in range(n):
    car, mileage, fuel = input().split("|")
    initial_car_dict[car] = [int(mileage)]
    initial_car_dict[car].append(int(fuel))

while True:
    command = input().split(" : ")
    action = command[0]

    if action == 'Stop':
        break

    elif action == 'Drive':
        car_drive = command[1]
        distance_drive = int(command[2])
        fuel_drive = int(command[3])
        if car_drive in initial_car_dict.keys():
            if initial_car_dict[car_drive][1] >= fuel_drive:
                initial_car_dict[car_drive][0] += distance_drive
                initial_car_dict[car_drive][1] -= fuel_drive
                print(f'{car_drive} driven for {distance_drive} kilometers. {fuel_drive} liters of fuel consumed.')
                if initial_car_dict[car_drive][0] >= 100000:
                    print(f'Time to sell the {car_drive}!')
                    del initial_car_dict[car_drive]

            else:
                print(f'Not enough fuel to make that ride')

    elif action == 'Refuel':
        car_refuel = command[1]
        fuel_refuel = int(command[2])
        initial_fuel = int(fuel_refuel)
        while initial_car_dict[car_refuel][1] < 75 and fuel_refuel != 0:
            initial_car_dict[car_refuel][1] += 1
            fuel_refuel -= 1
        print(f'{car_refuel} refueled with {initial_fuel - fuel_refuel} liters')

    elif action == 'Revert':
        car_revert = command[1]
        kilometers_revert = int(command[2])
        if (initial_car_dict[car_revert][0] - kilometers_revert) < 10000:
            initial_car_dict[car_revert][0] = 10000
        else:
            initial_car_dict[car_revert][0] -= kilometers_revert
            print(f'{car_revert} mileage decreased by {kilometers_revert} kilometers')
for car, mileage_fuel in initial_car_dict.items():
    print(f'{car} -> Mileage: {mileage_fuel[0]} kms, Fuel in the tank: {mileage_fuel[1]} lt.')
