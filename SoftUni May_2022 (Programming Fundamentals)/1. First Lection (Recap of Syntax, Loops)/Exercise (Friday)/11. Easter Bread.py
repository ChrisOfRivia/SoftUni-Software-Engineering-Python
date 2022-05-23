budget = float(input())
kg_flour = float(input())

loaves = 0
colored_eggs = 0

pack_of_eggs = kg_flour * 0.75

liter_milk = kg_flour + kg_flour * 0.25
milk_for_one_bread = liter_milk / 4

sum_price = kg_flour + pack_of_eggs + milk_for_one_bread

while budget > sum_price:
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -= loaves - 2
    budget -= sum_price

print(f"You made {loaves} loaves of Easter bread! "
      f"Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")





