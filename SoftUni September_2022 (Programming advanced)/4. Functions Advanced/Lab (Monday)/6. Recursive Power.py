def recursive_power(number, power):
    result = 1
    for _ in range(1, power + 1):
        result *= number

    return result
