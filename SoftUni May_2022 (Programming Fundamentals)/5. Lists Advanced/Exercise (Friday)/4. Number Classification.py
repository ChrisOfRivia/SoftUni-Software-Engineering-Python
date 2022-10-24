def seperate_with_comma(list_nums):
    return ', '.join(list_nums)


numbers = list(map(int, input().split(", ")))

positive_nums = [str(num) for num in numbers if num >= 0]
negative_nums = [str(num) for num in numbers if num < 0]
even_nums = [str(num) for num in numbers if num % 2 == 0]
odd_nums = [str(num) for num in numbers if num % 2 != 0]

print(f'Positive: {seperate_with_comma(positive_nums)}')
print(f'Negative: {seperate_with_comma(negative_nums)}')
print(f'Even: {seperate_with_comma(even_nums)}')
print(f'Odd: {seperate_with_comma(odd_nums)}')
