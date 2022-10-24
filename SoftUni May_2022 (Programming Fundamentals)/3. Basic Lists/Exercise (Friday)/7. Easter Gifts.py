gifts = input().split(" ")

command = input()

new_gifts = []
delimeter = " "
done = False

while command != "No Money":
    if command[:10] in "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command[11::]:
                gifts[i] = f'None{i}'
    elif command[:8] == "Required":
        number = command[-1]
        number = int(number)
        if number + 1 > (len(gifts)):
            pass
        else:
            gifts[number] = command[9:-2]
    elif command[:10] == "JustInCase":
        for l in range(len(gifts)):
            if l == gifts.index(gifts[-1]):
                gifts[l] = command[11::]
    command = input()
for m in range(1):
    for j in gifts:
        if j[:4]+str(m) == f'None'+str(m):
            continue
        else:
            print(j, end=" ")
            done = True
