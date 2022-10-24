strings = input().split(", ")

sort_lists = sorted(strings, key=lambda x: (-len(x), x))

print(sort_lists)