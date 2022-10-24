

phone_book = {}

while True:
    number = input()
    if number.isdigit():
        break
    else:
        number = number.split("-")
    name = number[0]
    phone_number = number[1]
    if name not in phone_book:
        phone_book[name] = ""
    phone_book[name] = phone_number

for contacts in range(int(number)):
    name_person = input()
    if name_person not in phone_book:
        print(f'Contact {name_person} does not exist.')
    else:
        print(f'{name_person} -> {phone_book[name_person]}')