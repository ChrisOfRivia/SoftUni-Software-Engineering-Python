# •	Опаковъчна хартия - 5.80 лв. за ролка
# •	Плат - 7.20 лв. за ролка
# •	Лепило - 1.20 лв. за литър

number_rolki = int(input())
number_plat = int(input())
liter_glue = float(input())
procent_discount = int(input()) / 100

price_rolki = number_rolki * 5.80
price_plat = number_plat * 7.20
price_glue = liter_glue * 1.20

whole_price = price_plat + price_glue + price_rolki
whole_price -= whole_price * procent_discount

print(f"{whole_price:.3f}")
