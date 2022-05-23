# •	Първата и третата цифра трябва да бъдат четни
# •	Втората цифра трябва да бъде просто число в диапазона [2...7]

first_num_highest = int(input())
second_num_highest = int(input())
third_num_highest = int(input())

for first_num in range(1, first_num_highest + 1):
    if first_num % 2 == 0:
        for second_num in range(2, second_num_highest + 1):
            if second_num in (2, 3, 5, 7):
                for third_num in range(1, third_num_highest + 1):
                    if third_num % 2 == 0:
                        print(f"{first_num} {second_num} {third_num}")
