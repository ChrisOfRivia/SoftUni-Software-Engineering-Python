num_commands = int(input())

car_park = set()

for commands in range(num_commands):
    type_command, car_id = input().split(", ")
    if type_command == 'IN':
        car_park.add(car_id)

    elif type_command == 'OUT':
        car_park.remove(car_id)

if car_park:
    print("\n".join(car_park))
else:
    print(f'Parking Lot is Empty')

