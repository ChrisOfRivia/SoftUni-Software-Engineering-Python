import re

string = input()

regex = r'(?P<surround>=|\/)(?P<place>[A-Z][A-Za-z]{2,})(?P=surround)'

match = [items.groupdict() for items in re.finditer(regex, string)]

destinations = [item['place'] for item in match]

length_points = 0

for place in destinations:
    length_points += len(place)

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {length_points}')
