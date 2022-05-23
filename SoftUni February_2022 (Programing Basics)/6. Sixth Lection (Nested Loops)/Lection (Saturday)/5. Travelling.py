money = 0

while True:
    destination = input()
    if destination == "End":
        break

    price_needed = float(input())
    money = 0
    
    while money < price_needed:
        save = float(input())
        money += save

    if money >= price_needed:
        print(f"Going to {destination}!")
