string_numbers = input().split(", ")


print([index for index, number in enumerate(string_numbers) if int(number) % 2 == 0])