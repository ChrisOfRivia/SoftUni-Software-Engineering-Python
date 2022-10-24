import re

regex = '(?P<seperator>#|\|)(?P<food>[A-Za-z ]+)(?P=seperator)(?P<date>\d{2}\/\d{2}\/\d{2})(?P=seperator)(?P<calories>\d+)(?P=seperator)'
text = input()

match = [food.groupdict() for food in re.finditer(regex, text)]

total_cal = sum([int(item['calories']) for item in match])

days = total_cal // 2000
print(f'You have food to last you for: {days} days!')

for products in match:
    print(f'Item: {products["food"]}, Best before: {products["date"]}, Nutrition: {products["calories"]}')