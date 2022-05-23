budget = float(input())
season = input()

place_for_sleep = ""
place_for_vacation = ""
price = 0

if budget <= 1000:
    place_for_sleep = "Camp"
    if season == "Summer":
        place_for_vacation = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        place_for_vacation = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place_for_sleep = "Hut"
    if season == "Summer":
        place_for_vacation = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        place_for_vacation = "Morocco"
        price = budget * 0.60
if budget > 3000:
    place_for_sleep = "Hotel"
    if season == "Summer":
        place_for_vacation = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        place_for_vacation = "Morocco"
        price = budget * 0.90

print(f"{place_for_vacation} - {place_for_sleep} - {price:.2f}")