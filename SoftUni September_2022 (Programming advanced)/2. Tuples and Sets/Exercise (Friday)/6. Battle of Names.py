n = int(input())

odd_set = set()
even_set = set()

odd_sum = 0
even_sum = 0

for i in range(1, n + 1):
    name = input()
    ascii_sum = 0
    for ch in name:
        ascii_sum += ord(ch)
    ascii_sum /= i
    if int(ascii_sum) % 2 == 0:
        even_set.add(int(ascii_sum))
        even_sum += int(ascii_sum)
    else:
        odd_set.add(int(ascii_sum))
        odd_sum += int(ascii_sum)

if even_sum == odd_sum:
    str_one = [str(el) for el in even_set.union(odd_set)]
    print(', '.join(str_one))
elif odd_sum > even_sum:
    str_two = [str(el) for el in odd_set.intersection(odd_set.symmetric_difference(even_set))]
    print(', '.join(str_two))
elif even_sum > odd_sum:
    str_three = [str(el) for el in even_set.symmetric_difference(odd_set)]
    print(', '.join(str_three))


