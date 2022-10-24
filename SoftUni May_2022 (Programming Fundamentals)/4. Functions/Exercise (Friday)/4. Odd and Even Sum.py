def sum_of_evens_and_odds(num):
    even_sum = 0
    odd_sum = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even_sum += i
        elif i % 2 != 0:
            odd_sum += i
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


number = input()
print(sum_of_evens_and_odds(number))