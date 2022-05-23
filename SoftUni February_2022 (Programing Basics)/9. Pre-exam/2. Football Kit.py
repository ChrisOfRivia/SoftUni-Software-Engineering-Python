# цената на шортите е 75% от цената на тениските
# цената на чорапите е 20% от цената на шортите
# Бутонките струват два пъти колкото тениската и шортите взети заедно
# отстъпка на стойност 15% от общата сума
# Ако сметката на Пепи е по-висока или равна на дадена сума,

price_of_shirt = float(input())
price_for_ball = float(input())

price_shorts = price_of_shirt * 0.75
price_socks = price_shorts * 0.20
price_shoes = (price_of_shirt + price_shorts) * 2

whole_sum = price_of_shirt + price_shorts + price_socks + price_shoes
whole_sum -= whole_sum * 0.15

if whole_sum >= price_for_ball:
    print(f"Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {whole_sum:.2f} lv.")
else:
    diff = abs(whole_sum - price_for_ball)
    print(f"No, he will not earn the world-cup replica ball.")
    print(f"He needs {diff:.2f} lv. more.")
