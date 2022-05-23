days_rented = int(input()) -1
type_of_shelter = input()
feedback = input()

price_for_one_night = 0
end_price = 0

if type_of_shelter == "room for one person":
    price_for_one_night = 18
    end_price = days_rented * price_for_one_night
elif type_of_shelter == "apartment":
    price_for_one_night = 25
    end_price = days_rented * price_for_one_night
    if days_rented < 10:
        end_price -= end_price * 0.30
    elif 10 <= days_rented <= 15:
        end_price -= end_price * 0.35
    elif days_rented > 15:
        end_price -= end_price * 0.50
elif type_of_shelter == "president apartment":
    price_for_one_night = 35
    end_price = days_rented * price_for_one_night
    if days_rented < 10:
        end_price -= end_price * 0.10
    elif 10 <= days_rented <= 15:
        end_price -= end_price * 0.15
    elif days_rented > 15:
        end_price -= end_price * 0.20

if feedback == "positive":
    end_price += end_price * 0.25
elif feedback == "negative":
    end_price -= end_price * 0.10

print(f"{end_price:.2f}")