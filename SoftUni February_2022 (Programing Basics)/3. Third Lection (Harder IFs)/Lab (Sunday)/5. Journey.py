budget = float(input())
season = input()

vacation = ""
costs = 0
place_to_sleep = ""

if budget <= 100:
    vacation = "Bulgaria"
    if season == "summer":
        place_to_sleep = "Camp"
        costs = budget * 0.30
    elif season == "winter":
        place_to_sleep = "Hotel"
        costs = budget * 0.70
elif 100 < budget <= 1000:
    vacation = "Balkans"
    if season == "summer":
        place_to_sleep = "Camp"
        costs = budget * 0.40
    elif season == "winter":
        place_to_sleep = "Hotel"
        costs = budget * 0.80
elif budget > 1000:
    vacation = "Europe"
    if season == "summer" or season == "winter":
        place_to_sleep = "Hotel"
        costs = budget * 0.90

print(f"Somewhere in {vacation}")
print(f"{place_to_sleep} - {costs:.2f}")