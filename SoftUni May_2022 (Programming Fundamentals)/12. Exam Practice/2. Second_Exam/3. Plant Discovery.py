n = int(input())

plants_rarity_dict = {}
plants_collection_rarity = {}

for i in range(n):
    plants, rarity = input().split('<->')
    plants_rarity_dict[plants] = int(rarity)
    plants_collection_rarity[plants] = []


while True:
    command = input().split(":")
    if ''.join(command) == 'Exhibition':
        break
    action = command[0]
    split = command[1].split('-')

    if action == 'Rate':
        plant = split[0][1:-1]
        if plant not in plants_rarity_dict.keys():
            print('error')
            continue
        rate = int(split[1][1::])
        plants_collection_rarity[plant].append(rate)

    elif action == 'Update':
        plant_update = split[0][1:-1]
        if plant_update not in plants_rarity_dict.keys():
            print('error')
            continue
        update = int(split[1][1::])
        plants_rarity_dict[plant_update] = update

    elif action == 'Reset':
        plant_reset = split[0][1::]
        if plant_reset not in plants_rarity_dict.keys():
            print('error')
            continue
        plants_collection_rarity[plant_reset] = []

print(f'Plants for the exhibition:')
for plant, rarity in plants_rarity_dict.items():
    if len(plants_collection_rarity[plant]) > 0:
        average_rarity = sum(plants_collection_rarity[plant]) / len(plants_collection_rarity[plant])
    else:
        average_rarity = 0
    print(f'- {plant}; Rarity: {rarity}; Rating: {average_rarity:.2f}')