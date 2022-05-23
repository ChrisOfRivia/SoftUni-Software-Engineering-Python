from math import floor, ceil

loze_kv_m = int(input())
grape_for_one_cubic_meter = float(input())
needed_liters_wine = int(input())
workers = int(input())

all_grapes = loze_kv_m * grape_for_one_cubic_meter

wine = (all_grapes * 0.40) / 2.5

diff = abs(needed_liters_wine - wine)
wine_per_person = diff / workers

if wine >= needed_liters_wine:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")