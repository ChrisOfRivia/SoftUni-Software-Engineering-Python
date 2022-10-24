def grocery_store(**kwargs):
    dict = {}
    result = ''

    sorting = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for items in sorting:
        dict[items[0]] = items[1]

    for key, value in dict.items():
        result += f"\n{key}: {value}"

    return result
