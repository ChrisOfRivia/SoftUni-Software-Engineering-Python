number_plays = int(input())

invalid_numbers = 0
num_numbers = 0
points = 0
percentages = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0

for each_play in range(number_plays):
    number = int(input())

    if number < 0 or number > 50:
        invalid_numbers += 1
        points /= 2
    else:
        num_numbers += 1

    if 0 <= number <= 9:
        from_0_to_9 += 1
        points += number * 0.20

    elif 10 <= number <= 19:
        from_10_to_19 += 1
        points += number * 0.30

    elif 20 <= number <= 29:
        from_20_to_29 += 1
        points += number * 0.40

    elif 30 <= number <= 39:
        from_30_to_39 += 1
        points += 50

    elif 40 <= number <= 50:
        from_40_to_50 += 1
        points += 100

percentage_0_9 = from_0_to_9 / number_plays * 100
percentage_10_19 = from_10_to_19 / number_plays * 100
percentage_20_29 = from_20_to_29 / number_plays * 100
percentage_30_39 = from_30_to_39 / number_plays * 100
percentage_40_50 = from_40_to_50 / number_plays * 100
percentage_invalid = invalid_numbers / number_plays * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percentage_0_9:.2f}%")
print(f"From 10 to 19: {percentage_10_19:.2f}%")
print(f"From 20 to 29: {percentage_20_29:.2f}%")
print(f"From 30 to 39: {percentage_30_39:.2f}%")
print(f"From 40 to 50: {percentage_40_50:.2f}%")
print(f"Invalid numbers: {percentage_invalid:.2f}%")