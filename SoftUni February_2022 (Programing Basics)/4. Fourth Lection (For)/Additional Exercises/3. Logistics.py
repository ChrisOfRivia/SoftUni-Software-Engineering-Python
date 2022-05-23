number_heavy_vehicles = int(input())

all_tons = 0
vehicle_microbus = 0
price_microbus = 200

vehicle_truck = 0
price_truck = 175

vehicle_train = 0
price_train = 120

for each_vehicle in range(number_heavy_vehicles):
    ton = int(input())
    all_tons += ton

    if 0 <= ton <= 3:
        vehicle_microbus += ton
    elif 4 <= ton <= 11:
        vehicle_truck += ton
    elif ton >= 12:
        vehicle_train += ton


all_money = ((vehicle_microbus * price_microbus) + (vehicle_truck * price_truck) + (vehicle_train * price_train))

average_money_a_ton = all_money / all_tons

percentage_microbus = vehicle_microbus / all_tons * 100
percentage_truck = vehicle_truck / all_tons * 100
percentage_train = vehicle_train / all_tons * 100

print(f"{average_money_a_ton:.2f}")
print(f"{percentage_microbus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")