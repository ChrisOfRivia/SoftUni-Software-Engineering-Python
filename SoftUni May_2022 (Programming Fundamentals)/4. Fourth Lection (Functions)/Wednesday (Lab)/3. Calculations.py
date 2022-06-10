operator = input()
first_number = int(input())
second_number = int(input())


def operations(a, b):
    if operator == 'multiply':
        return int(a * b)
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return int(a + b)
    elif operator == 'subtract':
        return int(a - b)


print(operations(first_number, second_number))









