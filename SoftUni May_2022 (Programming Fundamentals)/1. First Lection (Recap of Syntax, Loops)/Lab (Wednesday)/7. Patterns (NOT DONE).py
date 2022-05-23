n = int(input())

for first_part in range(0, n + 1):
    print("*" * first_part)
for second_part in range(n - 1, 0, -1):
    print("*" * second_part)