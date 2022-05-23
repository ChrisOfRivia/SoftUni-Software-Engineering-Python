# •	IP – 499.99 лева.
# •	Normal – 249.99 лева.

# • От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.

budget = float(input())
category = input()
people_in_group = int(input())

transport_money = 0
price_for_match = 0


if category == "VIP":
    price_for_match = 499.99
    if 1 <= people_in_group <= 4:
        transport_money = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport_money = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport_money = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport_money = budget * 0.40
    elif people_in_group >= 50:
        transport_money = budget * 0.25

elif category == "Normal":
    price_for_match = 249.99
    if 1 <= people_in_group <= 4:
        transport_money = budget * 0.75
    elif 5 <= people_in_group <= 9:
        transport_money = budget * 0.60
    elif 10 <= people_in_group <= 24:
        transport_money = budget * 0.50
    elif 25 <= people_in_group <= 49:
        transport_money = budget * 0.40
    elif people_in_group >= 50:
        transport_money = budget * 0.25

money_left = budget - transport_money

every_ticket = price_for_match * people_in_group

diff = abs(money_left - every_ticket)

if money_left >= every_ticket:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
