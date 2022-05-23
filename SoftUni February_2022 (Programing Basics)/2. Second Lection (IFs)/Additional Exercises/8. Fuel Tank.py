type_fuel = input()
fuel = float(input())

fuel_type = ""

if type_fuel == "Diesel":
    if fuel < 25:
        print("Fill your tank with diesel!")
    else:
        print(f"You have enough diesel.")
elif type_fuel == "Gasoline":
    if fuel < 25:
        print("Fill your tank with gasoline!")
    else:
        print(f"You have enough gasoline.")
elif type_fuel == "Gas":
    if fuel < 25:
        print("Fill your tank with gas!")
    else:
        print(f"You have enough gas.")
else:
    print("Invalid fuel!")