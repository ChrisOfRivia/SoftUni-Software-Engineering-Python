def multiplication_negative_positive_or_zero(a, b, c):
    if a < 0 and b < 0 and c < 0:
        state = 'negative'
    elif a > 0 and b > 0 and c > 0:
        state = 'positive'
    elif a < 0 < b and c > 0 or a > 0 > b and c > 0 or a > 0 > c and b > 0:
        state = 'negative'
    else:
        state = 'positive'
    if a == 0 or b == 0 or c == 0:
        state = 'zero'
    return state


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(multiplication_negative_positive_or_zero(first_num, second_num, third_num))