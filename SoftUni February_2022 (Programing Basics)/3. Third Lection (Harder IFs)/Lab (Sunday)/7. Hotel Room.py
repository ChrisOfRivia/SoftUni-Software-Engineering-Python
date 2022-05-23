month = input()
number_nights = int(input())

studio = 0
apartment = 0
costs = 0

if month in "May, October":
    studio = 50
    apartment = 65
    if 7 < number_nights <= 14:
        studio -= studio * 0.05
    elif number_nights > 14:
        studio -= studio * 0.30
        apartment -= apartment * 0.10
if month in "June, September":
    studio = 75.20
    apartment = 68.70
    if number_nights > 14:
        studio -= studio * 0.20
        apartment -= apartment * 0.10
if month in "July, August":
    studio = 76
    apartment = 77
    if number_nights > 14:
        apartment -= apartment * 0.10

full_price_apartments = number_nights * apartment
full_price_studio = number_nights * studio

print(f"Apartment: {full_price_apartments:.2f} lv.")
print(f"Studio: {full_price_studio:.2f} lv.")