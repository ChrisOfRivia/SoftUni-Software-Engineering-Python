#Chicken = 10.35lv
#Fish = 12.40lv
#Vegetarian = 8.15lv

Chicken_menus = int(input())
Fish_menus = int(input())
Vegetarian_menus = int(input())

price_for_chicken = Chicken_menus * 10.35
price_for_fish = Fish_menus * 12.40
price_for_vegetarian = Vegetarian_menus * 8.15

whole_sum = price_for_vegetarian + price_for_fish + price_for_chicken

price_of_desert = whole_sum * 0.20
price_of_dostavka = 2.50

whole_whole_sum = whole_sum + price_of_desert + price_of_dostavka

print(whole_whole_sum)