def forecast(*args):
    forecast_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    string = ''

    for city, weather in args:
        if weather == 'Sunny':
            forecast_dict['Sunny'].append(city)

        elif weather == 'Cloudy':
            forecast_dict['Cloudy'].append(city)

        elif weather == 'Rainy':
            forecast_dict['Rainy'].append(city)

    for key, value in forecast_dict.items():
        if value:
            for weathers in sorted(value):
                string += f"{weathers} - {key}\n"

    return string


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
