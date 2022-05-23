pens = int(input())
markers = int(input())
preparat_liters = int(input())
discount_percent = int(input()) / 100

price_of_pens = pens * 5.80
price_of_markers = markers * 7.20
price_of_preparat = preparat_liters * 1.20

whole_price = price_of_pens + price_of_markers + price_of_preparat
discount = whole_price - (whole_price * discount_percent)

print(discount)