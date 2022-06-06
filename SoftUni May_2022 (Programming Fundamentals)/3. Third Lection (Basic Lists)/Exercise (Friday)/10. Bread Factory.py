string = input().split("|")
energy = 100
coins = 100
over = False

for i in string:
    each_order = i.split("-")
    event = each_order[0]
    number = int(each_order[1])
    if event == 'rest':
        temp_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = abs(temp_energy - energy)
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')
    elif event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
            continue
    else:
        if coins >= number:
            coins -= number
            print(f'You bought {event}.')
        else:
            print(f'Closed! Cannot afford {event}.')
            over = True
            break
if not over:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
