elements = input().split()

stock = {}

for i in range(0, len(elements), 2):
    product = elements[i]
    in_stock = elements[i + 1]
    stock[product] = int(in_stock)

print(stock)
