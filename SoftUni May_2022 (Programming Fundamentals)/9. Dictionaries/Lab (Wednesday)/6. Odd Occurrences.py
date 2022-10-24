elements = input().split()

odd_keys = []
count_dict = {}

for el in elements:
    el = el.lower()
    if el not in count_dict:
        count_dict[el] = 0
    count_dict[el] += 1

for key, value in count_dict.items():
    if value % 2 != 0:
        odd_keys.append(key)
    else:
        pass

print(*odd_keys, sep=" ")
