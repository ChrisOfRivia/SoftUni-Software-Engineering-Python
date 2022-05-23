age_of_lily = int(input())
price_of_washing_machine = float(input())
price_for_one_toy = int(input())

even_money = 0
odd_toys = 0
brothers_money = 1

for i in range(1, age_of_lily + 1):
    if i % 2 == 0:
        even_money += ((i * 10) / 2) - brothers_money
    else:
        odd_toys += 1

toys_sold = odd_toys * price_for_one_toy

diff = abs((even_money + toys_sold) - price_of_washing_machine)

if (even_money + toys_sold) >= price_of_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
