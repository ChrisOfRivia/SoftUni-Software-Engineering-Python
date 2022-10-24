all_products = input().split()
stock = {}

for i in range(0, len(all_products), 2):
    product = all_products[i]
    quantity = all_products[i + 1]
    stock[product] = int(quantity)

search_elements = input().split()

for el in search_elements:
    if el not in stock:
        print(f'Sorry, we don\'t have {el}')
    else:
        print(f'We have {stock.get(el)} of {el} left')