from math import ceil, floor

num_magnolii = int(input())
num_zumbul = int(input())
num_roses = int(input())
num_cacti = int(input())
gift_price = float(input())

sum_flowers = num_magnolii * 3.25 + num_zumbul * 4 + num_roses * 3.50 + num_cacti * 8

tax = sum_flowers - sum_flowers * 0.05

diff = abs(tax - gift_price)

if gift_price > tax:
    print(f"She will have to borrow {ceil(diff)} leva.")
else:
    print(f"She is left with {floor(diff)} leva.")