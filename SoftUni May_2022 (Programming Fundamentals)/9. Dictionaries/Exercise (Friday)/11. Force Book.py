sides = {}

while True:
    force_user_and_side = input()

    if force_user_and_side == 'Lumpawaroo':
        break

    if " | " in force_user_and_side:
        split = force_user_and_side.split(" | ")
        side = split[0]
        user = split[1]
        present = False

        for value in sides.values():
            if user in value:
                present = True
                break
        if not present:
            if side not in sides:
                sides[side] = [user]
            else:
                sides[side].append(user)


    elif " -> " in force_user_and_side:
        split = force_user_and_side.split(" -> ")
        user = split[0]
        side = split[1]
        present = False

        for key, value in sides.items():
            if user in value:
                present = True
                sides[key].pop(value.index(user))
                break

        if side not in sides.keys():
            sides[side] = [user]
        else:
            sides[side].append(user)
        print(f'{user} joins the {side} side!')

for side in sides.keys():
    if len(sides[side]) > 0:
        print(f'Side: {side}, Members: {len(sides[side])}')
        for member in sides[side]:
            print(f'! {member}')
