annual_taksa = int(input())

basket_shoes = annual_taksa - (annual_taksa * 0.40)
basket_suit = basket_shoes - (basket_shoes * 0.20)
basket_ball = basket_suit * 1 / 4
basket_accessory = basket_ball * 1 / 5

whole_price = basket_accessory + basket_ball + basket_suit + basket_shoes

print(whole_price + annual_taksa)