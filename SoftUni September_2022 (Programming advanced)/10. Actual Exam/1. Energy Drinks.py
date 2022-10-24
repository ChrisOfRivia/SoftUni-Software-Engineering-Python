from collections import deque

mg_caffeine = deque(input().split(', '))
energy_drinks = deque(input().split(', '))

maximum_mg = 300
caffeine_for_day = 0

total_caffeine = 0

while mg_caffeine and energy_drinks:
    last_mg_caffeine = int(mg_caffeine[-1])
    first_energy_drink = int(energy_drinks[0])

    caffeine = last_mg_caffeine * first_energy_drink

    if caffeine + total_caffeine <= maximum_mg:
        total_caffeine += caffeine

        mg_caffeine.pop()
        energy_drinks.popleft()

    else:
        mg_caffeine.pop()
        energy_drinks.rotate(-1)
        if total_caffeine > 30:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(energy_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")







