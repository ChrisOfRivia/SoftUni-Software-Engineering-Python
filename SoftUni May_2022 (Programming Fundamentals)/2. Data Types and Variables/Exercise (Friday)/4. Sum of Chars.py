times = int(input())

symbol_sum = 0

for _ in range(times):
    symbol = input()
    symbol_sum += ord(symbol)

print(f'The sum equals: {symbol_sum}')