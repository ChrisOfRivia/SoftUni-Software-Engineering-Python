num_excursions_sea = int(input())
num_excursions_mountain = int(input())

price_sea = 680
price_mountain = 499
profit = 0
everything_sold = False

while True:
    name_of_packet = input()
    if name_of_packet == "Stop":
        break
    if name_of_packet == "sea":
        if num_excursions_sea > 0:
            profit += 680
            num_excursions_sea -= 1
        else:
            pass
    elif name_of_packet == "mountain":
        if num_excursions_mountain > 0:
            profit += 499
            num_excursions_mountain -= 1
        else:
            pass

    if num_excursions_mountain == 0 and num_excursions_sea == 0:
        everything_sold = True
        break

if everything_sold:
    print(f"Good job! Everything is sold.")
    print(f"Profit: {profit} leva.")
else:
    print(f"Profit: {profit} leva.")
