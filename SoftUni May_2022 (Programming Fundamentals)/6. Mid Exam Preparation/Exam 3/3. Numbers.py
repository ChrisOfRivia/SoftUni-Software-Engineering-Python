sequence_of_integers = list(map(int, input().split(" ")))
over_average = []
counter = 0

average_sum = sum(sequence_of_integers) / len(sequence_of_integers)

for nums in sequence_of_integers:
    if nums > average_sum:
        over_average.append(nums)
    else:
        counter += 1

if not over_average and counter > 0:
    print('No')

while len(over_average) > 5:
    over_average.remove(min(over_average))

over_average.sort()
print(*over_average[::-1], sep=" ")
