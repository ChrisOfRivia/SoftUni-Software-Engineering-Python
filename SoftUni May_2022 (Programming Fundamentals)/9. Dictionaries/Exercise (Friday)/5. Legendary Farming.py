junk = {}
built = False
farming = {'shards': 0, 'fragments': 0, 'motes': 0}

while True:
    list_of_items = input().split(" ")

    for i in range(0, len(list_of_items), 2):
        item = list_of_items[i + 1]
        quantity_of_item = int(list_of_items[i])
        item = item.lower()
        if item not in farming:
            if item not in junk:
                junk[item] = 0
            junk[item] += quantity_of_item
        else:
            farming[item] += quantity_of_item
        if farming['shards'] >= 250 or farming['motes'] >= 250 or farming['fragments'] >= 250:
            built = True
            break
    if built:
        break

if farming['shards'] >= 250:
    farming['shards'] -= 250
    print(f'Shadowmourne obtained!')
elif farming['fragments'] >= 250:
    farming['fragments'] -= 250
    print(f'Valanyr obtained!')
elif farming['motes'] >= 250:
    farming['motes'] -= 250
    print(f'Dragonwrath obtained!')

for key, value in farming.items():
    key = key.lower()
    print(f'{key}: {value}')

for key, value in junk.items():
    key = key.lower()
    print(f'{key}: {value}')