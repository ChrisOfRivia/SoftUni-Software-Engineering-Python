kilometers = int(input())
type_of_day = input()

price = 0

if 0 < kilometers < 20:
    if type_of_day == "day":
        price = 0.70 + kilometers * 0.79
    elif type_of_day == "night":
        price = 0.70 + kilometers * 0.90
elif 20 <= kilometers < 100:
    if type_of_day == "day" or "night":
        price = 0.09 * kilometers
elif kilometers >= 100:
    price = 0.06 * kilometers

print(f"{price:.2f}")