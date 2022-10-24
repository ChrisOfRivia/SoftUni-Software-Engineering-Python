population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

evenly_distributed = False
ran_out_of_money = False
counter = 0

for index, each_person in enumerate(population):
    if population[index] < minimum_wealth:
        while population[index] != minimum_wealth:
            highest_number_index = population.index(max(population))
            if population[highest_number_index] - (minimum_wealth - population[index]) <= 0:
                ran_out_of_money = True
                break
            else:
                population[highest_number_index] -= abs(population[index] - minimum_wealth)
                population[index] += abs(population[index] - minimum_wealth)
    if ran_out_of_money:
        break

for checking_money_per_person in population:
    if checking_money_per_person < minimum_wealth:
        counter += 1

if counter < len(population) and counter != 0:
    evenly_distributed = False
else:
    evenly_distributed = True


if evenly_distributed:
    print(population)
else:
    print(f'No equal distribution possible')
