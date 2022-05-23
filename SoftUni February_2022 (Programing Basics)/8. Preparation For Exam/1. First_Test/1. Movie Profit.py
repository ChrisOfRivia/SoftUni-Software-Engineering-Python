name_of_film = input()
num_days = int(input())
num_tickets = int(input())
price_of_ticket = float(input())
percent_for_theatre = int(input()) / 100

sum_for_one_day = num_tickets * price_of_ticket
whole_period_sum = num_days * sum_for_one_day

percent_for_theatre_money = whole_period_sum * percent_for_theatre

prihod_from_film = whole_period_sum - percent_for_theatre_money

print(f"The profit from the movie {name_of_film} is {prihod_from_film:.2f} lv.")