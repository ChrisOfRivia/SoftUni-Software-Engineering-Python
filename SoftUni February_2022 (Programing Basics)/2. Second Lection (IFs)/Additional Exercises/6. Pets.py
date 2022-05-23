from math import floor, ceil

days = int(input())
left_food_kg = int(input())
food_a_day_dog_kg = float(input())
food_a_day_cat_kg = float(input())
food_a_day_turtle_gr = float(input())

needed_food_dog = days * food_a_day_dog_kg
needed_food_cat = days * food_a_day_cat_kg
needed_food_turtle = days * food_a_day_turtle_gr / 1000

whole_food = needed_food_turtle + needed_food_cat + needed_food_dog

diff = abs(whole_food - left_food_kg)

if whole_food <= left_food_kg:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
