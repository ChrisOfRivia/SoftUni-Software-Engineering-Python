people = []

while True:
    line = input()

    if line == 'End':
        print(f"{len(people)} people remaining.")
        break
    elif line == 'Paid':
        print('\n'.join(people))
        people.clear()
    else:
        people.append(line)

