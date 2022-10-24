n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(input()))

symbol_found = False
group_idx = -1
symbol_idx = -1

while True:
    symbol_for_search = input()
    for each_group in matrix:
        group_idx += 1
        for each_symbol in each_group:
            symbol_idx += 1
            if symbol_for_search == each_symbol:
                print(f"({group_idx}, {symbol_idx})")
                symbol_found = True
                break
        symbol_idx = -1
        if symbol_found:
            break
        elif not symbol_found and group_idx + 1 == len(matrix):
            break
    if symbol_found:
        break
    elif not symbol_found and group_idx + 1 == len(matrix):
        break

if not symbol_found:
    print(f"{symbol_for_search} does not occur in the matrix")