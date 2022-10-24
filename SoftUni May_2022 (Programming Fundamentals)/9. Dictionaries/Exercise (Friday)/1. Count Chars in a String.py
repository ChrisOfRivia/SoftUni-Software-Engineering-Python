chars = input().split(" ")

count_chars = {}
long_txt = ""

for items in chars:
    long_txt += items

for each_letter in long_txt:
    if each_letter not in count_chars:
        count_chars[each_letter] = 0
    count_chars[each_letter] += 1

for key, value in count_chars.items():
    print(f'{key} -> {value}')