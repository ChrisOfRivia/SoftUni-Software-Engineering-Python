def func_executor(*args):
    result = ''

    for func in args:
        result += f"\n{func[0].__name__} - {func[0](*func[1])}"

    return result