# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши),
# таксата  намалява с 25%. Организаторите отделят 5% процента от събраната сума за разходи.

num_juniors = int(input())
num_seniors = int(input())
type_race = input()

all_cyclists = num_seniors + num_juniors
price_for_juniors = 0
price_for_seniors = 0
tax = False

if type_race == "trail":
    price_for_juniors = 5.50
    price_for_seniors = 7
elif type_race == "cross-country":
    price_for_juniors = 8
    price_for_seniors = 9.50
    if all_cyclists >= 50:
        Tax = True
        price_for_seniors -= price_for_seniors * 0.25
        price_for_juniors -= price_for_juniors * 0.25
elif type_race == "downhill":
    price_for_juniors = 12.25
    price_for_seniors = 13.75
elif type_race == "road":
    price_for_juniors = 20
    price_for_seniors = 21.50

juniors_money = price_for_juniors * num_juniors
seniors_money = price_for_seniors * num_seniors

whole_money = juniors_money + seniors_money

tax = whole_money - whole_money * 0.05

print(f"{tax:.2f}")