import re

regex = r'>>([A-Za-z]+)<<(\d+[\.\d]*)!(\d+)'
total_price = 0
bought_items = []

while True:
    furniture = input()
    if furniture == 'Purchase':
        break
    matches = re.findall(regex, furniture)

    for match in matches:
        type_furniture = match[0]
        price_furniture = float(match[1])
        quantity_furniture = int(match[2])

        total_price += price_furniture * quantity_furniture
        bought_items.append(type_furniture)

print(f'Bought furniture:')
for furniture in bought_items:
    print(furniture)
print(f'Total money spend: {total_price:.2f}')