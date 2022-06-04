n = int(input())

even_nums = []
odd_nums = []
negative_nums = []
positive_nums = []

for _ in range(n):
    numbers = int(input())
    if numbers >= 0:
        positive_nums.append(numbers)
        if numbers % 2 == 0 or numbers == 0:
            even_nums.append(numbers)
        elif numbers % 2 != 0:
            odd_nums.append(numbers)
    elif numbers < 0:
        negative_nums.append(numbers)
        if numbers % 2 == 0:
            even_nums.append(numbers)
        elif numbers % 2 != 0:
            odd_nums.append(numbers)
command = input()

if command == "even":
    print(even_nums)
elif command == "odd":
    print(odd_nums)
elif command == "negative":
    print(negative_nums)
elif command == "positive":
    print(positive_nums)