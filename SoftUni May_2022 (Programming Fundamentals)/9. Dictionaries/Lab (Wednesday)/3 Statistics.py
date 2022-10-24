pairs = input()

stock = {}

while not pairs == 'statistics':
    split = pairs.split(": ")
    product = split[0]
    quantity = split[1]
    if product not in stock:
        stock[product] = int(quantity)
    else:
        stock[product] += int(quantity)

    pairs = input()

print(f'Products in stock:')
for products in stock:
    print(f'- {products}: {stock.get(products)}')
print(f'Total Products: {len(stock)}')
print(f'Total Quantity: {sum(stock.values())}')
