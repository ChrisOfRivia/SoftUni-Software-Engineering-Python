ores = {}

while True:
    ore_type = input()
    if ore_type == 'stop':
        break
    ore_quantity = int(input())
    if ore_type not in ores:
        ores[ore_type] = 0
    ores[ore_type] += ore_quantity

for key, values in ores.items():
    print(f'{key} -> {values}')