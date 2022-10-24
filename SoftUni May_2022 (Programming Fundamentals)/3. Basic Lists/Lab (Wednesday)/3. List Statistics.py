n = int(input())

count_positive = 0
sum_negative = 0

positive_list = []
negative_list = []

for _ in range(n):
    numbers = int(input())
    if numbers > 0:
        count_positive += 1
        positive_list.append(numbers)
    elif numbers <= 0:
        sum_negative += numbers
        negative_list.append(numbers)
print(positive_list)
print(negative_list)
print(f"Count of positives: {count_positive}")
print(f"Sum of negatives: {sum_negative}")
