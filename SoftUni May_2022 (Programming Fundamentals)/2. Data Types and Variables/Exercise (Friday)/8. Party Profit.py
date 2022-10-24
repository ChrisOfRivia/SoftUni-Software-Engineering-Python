companions = int(input())
days_of_adventure = int(input())

coins = 0

for days in range(1, days_of_adventure + 1):
    if days % 10 == 0:
        companions -= 2
    if days % 15 == 0:
        companions += 5
    coins += 50
    coins -= 2 * companions
    if days % 3 == 0:
        coins -= 3 * companions
    if days % 5 == 0:
        if days % 3 == 0:
            coins -= 2 * companions
        coins += 20 * companions
each_companion = int(coins / companions)
print(f'{companions} companions received {each_companion} coins each.')

