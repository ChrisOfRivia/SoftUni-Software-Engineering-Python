needed_nylon = int(input())
needed_paint = int(input())
needed_razreditel = int(input())
hours = int(input())

price_for_nylon = (needed_nylon + 2) * 1.50
price_of_paint = (needed_paint + needed_paint * 0.10) * 14.50
price_of_razreditel = needed_razreditel * 5.00
price_for_torbichki = 0.40

whole_sum = price_for_torbichki + price_for_nylon + price_of_paint + price_of_razreditel
sum_for_workers = (whole_sum * 0.30) * hours
end_sum = whole_sum + sum_for_workers

print(end_sum)
