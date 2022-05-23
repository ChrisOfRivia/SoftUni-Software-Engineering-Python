price_for_trip = float(input())
number_of_puzzle = int(input())
number_of_talking_doll = int(input())
number_of_teddy_bear = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

sum_price_of_toys = number_of_puzzle * 2.60 + number_of_talking_doll * 3 + number_of_teddy_bear * 4.10 \
                    + number_of_minions * 8.20 + number_of_trucks * 2
number_of_toys = number_of_puzzle + number_of_talking_doll + number_of_teddy_bear + number_of_minions + number_of_trucks
discount = 0

if number_of_toys >= 50:
    discount = sum_price_of_toys * 0.25
    sum_price_of_toys = sum_price_of_toys - discount

rent = sum_price_of_toys * 0.10
profit = sum_price_of_toys - rent

diff = abs(profit - price_for_trip)

if profit >= price_for_trip:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")