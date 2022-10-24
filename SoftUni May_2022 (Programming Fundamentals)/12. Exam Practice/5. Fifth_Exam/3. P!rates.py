city_pop_gold = {}
done = False

while True:
    command = input().split('||')
    action = command[0]
    if action == 'Sail':
        break
    city = action
    population = int(command[1])
    gold = int(command[2])
    if city not in city_pop_gold:
        city_pop_gold[city] = [population]
        city_pop_gold[city].append(gold)
    else:
        city_pop_gold[city][0] += population
        city_pop_gold[city][1] += gold

while True:
    new_command = input().split('=>')
    new_action = new_command[0]
    if new_action == 'End':
        if len(city_pop_gold) > 0:
            print(f'Ahoy, Captain! There are {len(city_pop_gold)} wealthy settlements to go to:')
            for town, pop_wealth in city_pop_gold.items():
                print(f'{town} -> Population: {pop_wealth[0]} citizens, Gold: {pop_wealth[1]} kg')
        else:
            print(f'Ahoy, Captain! All targets have been plundered and destroyed!')
        break

    elif new_action == 'Plunder':
        town_plunder = new_command[1]
        people_plunder = int(new_command[2])
        gold_plunder = int(new_command[3])
        city_pop_gold[town_plunder][0] -= people_plunder
        city_pop_gold[town_plunder][1] -= gold_plunder
        print(f'{town_plunder} plundered! {gold_plunder} gold stolen, {people_plunder} citizens killed.')
        if city_pop_gold[town_plunder][0] == 0 or city_pop_gold[town_plunder][1] == 0:
            print(f'{town_plunder} has been wiped off the map!')
            del city_pop_gold[town_plunder]

    elif new_action == 'Prosper':
        town_prosper = new_command[1]
        gold_prosper = int(new_command[2])
        if gold_prosper < 0:
            print(f'Gold added cannot be a negative number!')
        else:
            city_pop_gold[town_prosper][1] += gold_prosper
            print(f'{gold_prosper} gold added to the city treasury. {town_prosper} now has {city_pop_gold[town_prosper][1]} gold.')