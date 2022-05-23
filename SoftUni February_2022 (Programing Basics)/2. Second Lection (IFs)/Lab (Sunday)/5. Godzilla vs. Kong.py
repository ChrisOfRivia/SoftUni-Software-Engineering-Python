budget = float(input())
number_actors = int(input())
clothes_for_one_actor = float(input())

sum_decor = budget * 0.10

sum_clothes = number_actors * clothes_for_one_actor

if number_actors > 150:
    sum_clothes -= sum_clothes * 0.10

decor_and_actors = sum_decor + sum_clothes

money_left = budget - decor_and_actors

diff = abs(money_left)

if decor_and_actors > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
elif decor_and_actors <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
