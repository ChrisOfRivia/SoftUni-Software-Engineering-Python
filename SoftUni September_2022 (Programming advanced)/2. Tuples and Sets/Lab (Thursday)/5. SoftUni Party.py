num_guests = int(input())

all_guests = set()

guests_who_arrived = set()

for guest in range(num_guests):
    code = input()
    if len(code) == 8:
        all_guests.add(code)

while True:
    arriving_guests = input()
    if arriving_guests == 'END':
        break
    if len(arriving_guests) == 8:
        if arriving_guests in all_guests:
            guests_who_arrived.add(arriving_guests)

print(len(all_guests.difference(guests_who_arrived)))
sorted_guests = sorted(all_guests.difference(guests_who_arrived))
print("\n".join(sorted_guests))




