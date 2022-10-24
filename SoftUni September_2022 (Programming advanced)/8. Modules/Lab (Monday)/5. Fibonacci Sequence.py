from Fibonacci_sequence import *

result = []

while True:
    command = input().split()
    if command[0] == 'Stop':
        break

    elif command[0] == 'Create':
        number_create = int(command[-1])
        result = fibonacci_sequence(number_create)
        print(*result, sep=" ")

    elif command[0] == 'Locate':
        number_locate = int(command[-1])
        if number_locate in result:
            print(f"The number - {number_locate} is at index {result.index(number_locate)}")
        else:
            print(f"The number {number_locate} is not in the sequence")
