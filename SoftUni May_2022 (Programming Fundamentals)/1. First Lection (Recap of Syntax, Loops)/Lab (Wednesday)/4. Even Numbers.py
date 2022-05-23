cycle = int(input())
negative_numbers = 0

for cycles in range(cycle):
    number = int(input())

    if number % 2 != 0:
        negative_numbers += 1
        print(f"{number} is odd!")
        break

if negative_numbers == 0:
    print("All numbers are even.")



