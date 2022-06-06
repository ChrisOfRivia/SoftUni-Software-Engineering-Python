items = input().split("|")
budget = int(input())

start_budget = budget

old_prices = []
new_prices = []

for each_item in items:
    current_item = each_item.split("->")
    type_of_item = current_item[0]
    price_of_item = current_item[1]
    if current_item[0] == 'Clothes' and float(current_item[1]) > 50.00:
        continue
    elif current_item[0] == 'Shoes' and float(current_item[1]) > 35.00:
        continue
    elif current_item[0] == 'Accessories' and float(current_item[1]) > 20.50:
        continue
    if budget < float(current_item[1]):
        for prices in old_prices:
            prices = float(prices)
            prices += prices * 0.40
            new_prices.append(prices)
            budget += prices
            print(f'{prices:.2f}', end=" ")
        break
    else:
        old_prices.append(current_item[1])
        budget -= float(current_item[1])
profit = abs(budget - start_budget)
print(f'\nProfit: {profit:.2f}')
if budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')