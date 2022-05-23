season = input()
km_a_month = float(input())

money_for_month = 0

if season == "Spring" or season == "Autumn":
    if km_a_month <= 5000:
        money_for_month = 0.75
    elif 5000 < km_a_month <= 10000:
        money_for_month = 0.95
    elif 10000 < km_a_month <= 20000:
        money_for_month = 1.45
elif season == "Summer":
    if km_a_month <= 5000:
        money_for_month = 0.90
    elif 5000 < km_a_month <= 10000:
        money_for_month = 1.10
    elif 10000 < km_a_month <= 20000:
        money_for_month = 1.45
elif season == "Winter":
    if km_a_month <= 5000:
        money_for_month = 1.05
    elif 5000 < km_a_month <= 10000:
        money_for_month = 1.25
    elif 10000 < km_a_month <= 20000:
        money_for_month = 1.45

paycheck = km_a_month * money_for_month * 4
paycheck -= paycheck * 0.10

print(f"{paycheck:.2f}")