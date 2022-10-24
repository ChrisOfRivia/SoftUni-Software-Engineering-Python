def calculate_price_of_product(item, number):
    if item == 'coffee':
        return f'{number * 1.50:.2f}'
    elif item == 'coke':
        return f'{number * 1.40:.2f}'
    elif item == 'water':
        return f'{number * 1.00:.2f}'
    elif item == 'snacks':
        return f'{number * 2.00:.2f}'


product = input()
num = int(input())
print(calculate_price_of_product(product, num))
