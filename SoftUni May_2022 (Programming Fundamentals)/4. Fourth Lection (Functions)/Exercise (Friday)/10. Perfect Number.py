def perfect_num(number):
    sum_perfect = 0
    for i in range(1, number):
        if number % i == 0:
            sum_perfect += i
    if sum_perfect == number:
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


num = int(input())
print(perfect_num(num))


