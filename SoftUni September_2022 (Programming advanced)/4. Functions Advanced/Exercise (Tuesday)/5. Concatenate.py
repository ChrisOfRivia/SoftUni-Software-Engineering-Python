def concatenate(*args, **kwargs):
    word = ''.join(args)

    for key, value in kwargs.items():
        word = word.replace(key, value)

    return word