def sorting_cheeses(**kwargs):
    result = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0], x[1]))

    string = ''
    first_cheese = True

    for items in result:
        if first_cheese:
            string += items[0]
            first_cheese = False
        else:
            string += f"\n{items[0]}"

        for nums in sorted(items[1]).__reversed__():
            string += f'\n{nums}'

    return string

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
