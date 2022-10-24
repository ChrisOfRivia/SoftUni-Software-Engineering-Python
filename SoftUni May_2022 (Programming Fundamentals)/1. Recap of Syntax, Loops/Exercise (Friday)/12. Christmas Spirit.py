quantity_decor = int(input())
days_until_christmas = int(input())
budget = 0
christmas_spirit = 0

ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15


for days in range(1, days_until_christmas + 1):
    if days % 11 == 0:
        quantity_decor += 2
    if days % 2 == 0:
        budget += ornament_set * quantity_decor
        christmas_spirit += 5
    if days % 3 == 0:
        budget += (tree_skirt + tree_garland) * quantity_decor
        christmas_spirit += 13
    if days % 5 == 0:
        budget += tree_lights * quantity_decor
        christmas_spirit += 17
        if days % 3 == 0:
            christmas_spirit += 30
    if days % 10 == 0:
        christmas_spirit -= 20
        budget += tree_skirt + tree_garland + tree_lights
if days_until_christmas % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
