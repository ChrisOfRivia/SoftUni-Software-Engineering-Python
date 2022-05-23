# Видеокарта = 250 лв
# Процесор = 35% от цената на закупените видеокарти
# Рам памет = 10% от цената на закупените видеокарти

budget = float(input())
number_graphic_cards = int(input())
number_gpu = int(input())
number_ram = int(input())

price_graphic_card = 250
price_gpu = (number_graphic_cards * price_graphic_card) * 0.35
price_ram = (number_graphic_cards * price_graphic_card) * 0.10

whole_sum = (price_graphic_card * number_graphic_cards) + (price_gpu * number_gpu) \
            + (price_ram * number_ram)

if number_graphic_cards > number_gpu:
    whole_sum -= whole_sum * 0.15

money_left = abs(budget - whole_sum)

if whole_sum <= budget:
    print(f"You have {money_left:.2f} leva left!")
else:
    print(f"Not enough money! You need {money_left:.2f} leva more!")
