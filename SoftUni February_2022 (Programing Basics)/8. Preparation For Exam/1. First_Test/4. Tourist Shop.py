budget = float(input())

product_counter = 0
money_spent_counter = 0
diff = 0

no_money = False

while True:
    if budget < 0:
        break
    name_of_product = input()
    if name_of_product == "Stop":
        break
    price_of_product = float(input())

    product_counter += 1
    if product_counter % 3 == 0:
        price_of_product /= 2

    if price_of_product <= budget:
        money_spent_counter += price_of_product
        budget -= price_of_product
        no_money = False
    elif price_of_product > budget:
        diff = abs(budget - price_of_product)
        no_money = True
        break
if no_money:
    print(f"You don't have enough money! ")
    print(f"You need {diff:.2f} leva!")
elif not no_money:
    print(f"You bought {product_counter} products for {money_spent_counter:.2f} leva.")