century = int(input())

years = century * 100
days = years * 365.2422
hours = int(days) * 24
minutes = hours * 60

print(f'{int(century)} centuries = {int(years)} years = {int(days)} days = {int(hours)} hours = {int(minutes)} minutes')