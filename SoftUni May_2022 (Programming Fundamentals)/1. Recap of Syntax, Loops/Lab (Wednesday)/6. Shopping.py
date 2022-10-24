budget = int(input())
overdraft = False

while True:
    products = input()

    if products == "End":
        break
    else:
        products = int(products)

    if products > budget:
        print("You went in overdraft!")
        overdraft = True
        break

    budget -= products

if not overdraft:
    print("You bought everything needed.")