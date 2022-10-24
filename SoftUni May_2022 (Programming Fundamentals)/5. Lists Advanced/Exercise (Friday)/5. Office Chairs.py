rooms = int(input())

not_full = False
excess_chairs = 0

for each_room in range(1, rooms + 1):
    chair_counter = 0
    chairs_and_visitors = input().split()
    chairs = chairs_and_visitors[0]
    for num_chairs in chairs:
        chair_counter += 1
    visitors = int(chairs_and_visitors[1])
    if chair_counter > visitors:
        excess_chairs += abs(chair_counter - visitors)
    elif chair_counter == visitors:
        continue
    else:
        not_full = True
        print(f'{abs(chair_counter - visitors)} more chairs needed in room {each_room}')

if not not_full:
    print(f'Game On, {excess_chairs} free chairs left')
