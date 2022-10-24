countries = input().split(", ")
capitals = input().split(", ")

capitals_dict = {country: capital for country, capital in zip(countries, capitals)}

for country, capital in capitals_dict.items():
    print(f'{country} -> {capital}')
