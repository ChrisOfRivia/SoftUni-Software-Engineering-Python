inherited_money = float(input())
year_to_live_to = int(input())

years_now = 18

for years in range(1800, year_to_live_to + 1):
    if years % 2 == 0:
        inherited_money -= 12000
    else:
        inherited_money -= 12000 + years_now * 50

    years_now += 1


if inherited_money >= 0:
    print(f"Yes! He will live a carefree"
          f" life and will have {abs(inherited_money):.2f} dollars left." )
else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")