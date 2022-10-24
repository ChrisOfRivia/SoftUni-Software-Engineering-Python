def shopping_cart(*args):
    meals = {'Pizza': [], 'Soup': [], 'Dessert': []}

    string = ''
    valid_products = False

    for every_item in args:
        if every_item == 'Stop':
            break

        elif every_item[1] not in meals[every_item[0]]:

            if not meals[every_item[0]]:
                meals[every_item[0]].append(every_item[1])

            elif every_item[0] == 'Soup' and len(meals['Soup']) < 3:
                meals['Soup'].append(every_item[1])

            elif every_item[0] == 'Pizza' and len(meals['Pizza']) < 4:
                meals['Pizza'].append(every_item[1])

            elif every_item[0] == 'Dessert' and len(meals['Dessert']) < 2:
                meals['Dessert'].append(every_item[1])
            valid_products = True

    meals = dict(sorted(meals.items(), key=lambda x: (-len(x[1]), x[0])))

    if valid_products:
        for item, product in meals.items():
            string += f'{item}:\n'
            for items in sorted(product):
                string += f" - {items}\n"

        return string

    else:
        return 'No products in the cart!'
