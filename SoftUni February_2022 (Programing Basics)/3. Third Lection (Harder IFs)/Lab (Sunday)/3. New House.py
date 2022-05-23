type_flower = input()
number_flowers = int(input())
budget = int(input())

costs = 0

if type_flower == "Roses":
    costs = number_flowers * 5
    if number_flowers > 80:
        costs -= costs * 0.10
elif type_flower == "Dahlias":
    costs = number_flowers * 3.80
    if number_flowers > 90:
        costs -= costs * 0.15
elif type_flower == "Tulips":
    costs = number_flowers * 2.80
    if number_flowers > 80:
        costs -= costs * 0.15
elif type_flower == "Narcissus":
    costs = number_flowers * 3
    if number_flowers < 120:
        costs += costs * 0.15
elif type_flower == "Gladiolus":
    costs = number_flowers * 2.50
    if number_flowers < 80:
        costs += costs * 0.20


leftover_money = abs(budget - costs)

if budget >= costs:
    print(f"Hey, you have a great garden "
          f"with {number_flowers} {type_flower} and {leftover_money:.2f} leva left.")
else:
    print(f"Not enough money, you need {leftover_money:.2f} leva more.")
