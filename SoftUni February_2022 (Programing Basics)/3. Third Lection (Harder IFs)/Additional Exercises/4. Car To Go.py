budget = float(input())
season = input()

class_of_car = ""
type_car = ""
price = 0

if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    class_of_car = "Luxury class"
    type_car = "Jeep"
    price = budget * 0.90

print(f"{class_of_car}")
print(f"{type_car} - {price:.2f}")