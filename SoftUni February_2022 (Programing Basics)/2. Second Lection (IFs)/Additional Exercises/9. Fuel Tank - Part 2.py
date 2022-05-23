# •	Бензин – 2.22 лева за един литър,
# •	Дизел – 2.33 лева за един литър
# •	Газ – 0.93 лева за литър

# намаления за литър гориво: 18 ст.
# за литър дизел и 8 ст. за литър газ.

type_fuel = input()
amount_fuel = float(input())
discount_ticket = input()

price = 0

if type_fuel == "Gas":
    price = 0.93
    if discount_ticket == "Yes":
        price -= 0.08
    else:
        pass
    if 20 <= amount_fuel <= 25:
        price *= amount_fuel
        price -= price * 0.08
    elif amount_fuel > 25:
        price *= amount_fuel
        price -= price * 0.10
    else:
        price *= amount_fuel
elif type_fuel == "Diesel":
    price = 2.33
    if discount_ticket == "Yes":
        price -= 0.12
    else:
        pass
    if 20 <= amount_fuel <= 25:
        price *= amount_fuel
        price -= price * 0.08
    elif amount_fuel > 25:
        price *= amount_fuel
        price -= price * 0.10
    else:
        price *= amount_fuel
if type_fuel == "Gasoline":
    price = 2.22
    if discount_ticket == "Yes":
        price -= 0.18
    else:
        pass
    if 20 < amount_fuel <= 25:
        price *= amount_fuel
        price -= price * 0.08
    elif amount_fuel > 25:
        price *= amount_fuel
        price -= price * 0.10
    else:
        price *= amount_fuel

print(f"{price:.2f} lv.")