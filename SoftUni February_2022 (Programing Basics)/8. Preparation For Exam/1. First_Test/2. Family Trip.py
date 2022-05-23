budget = float(input())
num_sleepovers = int(input())
price_for_sleepover = float(input())
percent_additional_spending = int(input()) / 100

if num_sleepovers > 7:
    price_for_sleepover -= price_for_sleepover * 0.05

whole_price = num_sleepovers * price_for_sleepover
additional_spepnding = budget * percent_additional_spending

diff = abs(whole_price + additional_spepnding - budget)

if whole_price + additional_spepnding <= budget:
    print(f"Ivanovi will be left with {diff:.2f} leva after vacation.")
else:
    print(f"{diff:.2f} leva needed.")