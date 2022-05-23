type_of_screening = input()
rows = int(input())
columns = int(input())

ticket_price = 0
income = 0

if type_of_screening == "Premiere":
    ticket_price = 12
elif type_of_screening == "Normal":
    ticket_price = 7.50
elif type_of_screening == "Discount":
    ticket_price = 5.00

all_seats = rows * columns
income = ticket_price * all_seats

print(f"{income:.2f} leva")
