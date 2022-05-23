word = input()

end_sum = 0

for ch in word:
    if ch == "a":
        end_sum += 1
    if ch == "e":
        end_sum += 2
    if ch == "i":
        end_sum += 3
    if ch == "o":
        end_sum += 4
    if ch == "u":
        end_sum += 5

print(end_sum)