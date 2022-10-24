def factorial_number(num):
    for i in range(1, num):
        num *= i

    return num


first_number = int(input())
second_number = int(input())
divide = factorial_number(first_number) / factorial_number(second_number)
print(f'{divide:.2f}')