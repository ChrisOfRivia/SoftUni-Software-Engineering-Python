num_bought_hrizantemi = int(input())
num_bought_roses = int(input())
num_bought_tulips = int(input())
season = input()
if_holiday = input()

price_for_hrizanetma = 0
price_for_rose = 0
price_for_tulip = 0
whole_price = 0
num_all_flowers = num_bought_roses + num_bought_tulips + num_bought_hrizantemi


if season in "Spring, Summer":
    price_for_hrizanetma = 2
    price_for_rose = 4.10
    price_for_tulip = 2.50
    if if_holiday == "Y":
        price_for_hrizanetma += price_for_hrizanetma * 0.15
        price_for_rose += price_for_rose * 0.15
        price_for_tulip += price_for_tulip * 0.15
    else:
        pass

    full_price_hrizantema = price_for_hrizanetma * num_bought_hrizantemi
    full_price_roses = price_for_rose * num_bought_roses
    full_price_tulips = price_for_tulip * num_bought_tulips

    whole_price = full_price_roses + full_price_tulips + full_price_hrizantema

    if num_bought_tulips > 7 and season == "Spring":
        whole_price -= whole_price * 0.05
    if num_all_flowers > 20 and season in "Spring, Summer, Autumn, Winter":
        whole_price -= whole_price * 0.20

elif season in "Autumn, Winter":
    price_for_hrizanetma = 3.75
    price_for_rose = 4.50
    price_for_tulip = 4.15
    if if_holiday == "Y":
        price_for_hrizanetma += price_for_hrizanetma * 0.15
        price_for_rose += price_for_rose * 0.15
        price_for_tulip += price_for_tulip * 0.15
    else:
        pass

    full_price_hrizantema = price_for_hrizanetma * num_bought_hrizantemi
    full_price_roses = price_for_rose * num_bought_roses
    full_price_tulips = price_for_tulip * num_bought_tulips

    whole_price = full_price_roses + full_price_tulips + full_price_hrizantema

    if num_bought_roses >= 10 and season == "Winter":
        whole_price -= whole_price * 0.10

    if num_all_flowers > 20 and season in "Spring, Summer, Autumn, Winter":
        whole_price -= whole_price * 0.20

print(f"{whole_price + 2:.2f}")