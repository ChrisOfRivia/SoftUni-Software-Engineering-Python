price_veg_for_kg = float(input())
price_fruit_for_kg = float(input())
veg_kg = int(input())
fruit_kg = int(input())

full_price_fruit = price_fruit_for_kg * fruit_kg
full_price_veg = price_veg_for_kg * veg_kg

turn_to_euro = (full_price_veg + full_price_fruit) / 1.94

print(format(turn_to_euro, ".2f"))

