product_list = input()

product_dict = {}

original_prices = {}

quantity_dict = {}

while not product_list == 'buy':
    split = product_list.split(" ")

    product = split[0]
    price = float(split[1])
    quantity = int(split[2])
    full_price = price * quantity

    if product not in quantity_dict:
        quantity_dict[product] = 0
    quantity_dict[product] += quantity

    if product not in original_prices:
        original_prices[product] = price

    elif product in original_prices and original_prices[product] != price:
        product_dict[product] = 0
        original_prices[product] = price
        full_price = quantity_dict[product] * price


    if product not in product_dict:
        product_dict[product] = 0
    product_dict[product] += full_price

    product_list = input()

for product, price in product_dict.items():
    print(f'{product} -> {price:.2f}')
