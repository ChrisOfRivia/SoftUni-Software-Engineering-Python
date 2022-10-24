def even_odd(*args):
    evens = []
    odds = []

    for nums in args[:-1:]:
        if nums % 2 == 0:
            evens.append(nums)
        else:
            odds.append(nums)

    if args[-1] == 'even':
        return evens
    elif args[-1] == 'odd':
        return odds