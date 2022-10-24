def even_odd_filter(**kwargs):
    numbers = {}

    for key, val in kwargs.items():
        if key == 'even':
            numbers[key] = [i for i in val if i % 2 == 0]

        elif key == 'odd':
            numbers[key] = [i for i in val if i % 2 != 0]

    return dict(sorted(numbers.items(), key=lambda x: -len(x[1])))