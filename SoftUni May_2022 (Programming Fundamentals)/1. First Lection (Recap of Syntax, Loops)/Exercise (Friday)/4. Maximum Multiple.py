divisor = int(input())
boundary = int(input())
n = 0

hidden_number = 0

for n in range(boundary, 0, -1):
    if n / divisor == int(n / divisor):
        hidden_number = n
        break

print(n)