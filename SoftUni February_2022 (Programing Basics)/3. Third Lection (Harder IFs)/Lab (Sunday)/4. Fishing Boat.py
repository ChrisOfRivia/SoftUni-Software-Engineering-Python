budget = int(input())
season = input()
number_fishers = int(input())

price_of_boat = 0

if season == "Spring":
    price_of_boat = 3000
    if number_fishers <= 6:
        price_of_boat -= price_of_boat * 0.10
    elif 7 <= number_fishers <= 11:
        price_of_boat -= price_of_boat * 0.15
    elif number_fishers >= 12:
        price_of_boat -= price_of_boat * 0.25
elif season == "Summer":
    price_of_boat = 4200
    if number_fishers <= 6:
        price_of_boat -= price_of_boat * 0.10
    elif 7 <= number_fishers <= 11:
        price_of_boat -= price_of_boat * 0.15
    elif number_fishers >= 12:
        price_of_boat -= price_of_boat * 0.25
elif season == "Autumn":
    price_of_boat = 4200
    if number_fishers <= 6:
        price_of_boat -= price_of_boat * 0.10
    elif 7 <= number_fishers <= 11:
        price_of_boat -= price_of_boat * 0.15
    elif number_fishers >= 12:
        price_of_boat -= price_of_boat * 0.25
elif season == "Winter":
    price_of_boat = 2600
    if number_fishers <= 6:
        price_of_boat -= price_of_boat * 0.10
    elif 7 <= number_fishers <= 11:
        price_of_boat -= price_of_boat * 0.15
    elif number_fishers >= 12:
        price_of_boat -= price_of_boat * 0.25

if number_fishers % 2 == 0 and season != "Autumn":
    price_of_boat -= price_of_boat * 0.05

diff = abs(budget - price_of_boat)

if budget >= price_of_boat:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")