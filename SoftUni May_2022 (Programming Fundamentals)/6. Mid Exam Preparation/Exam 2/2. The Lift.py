waiting_people = int(input())
state_of_train = list(map(int, input().split(" ")))
count = 0

for index, every_wagon in enumerate(state_of_train):
    while state_of_train[index] < 4 and waiting_people > 0:
        state_of_train[index] += 1
        waiting_people -= 1

for counter in state_of_train:
    if counter == 4:
        count += 1
        if count == len(state_of_train) and waiting_people == 0:
            print(*state_of_train, sep=" ")
        elif count == len(state_of_train) and waiting_people > 0:
            print(f'There isn\'t enough space! {waiting_people} people in a queue!')
            print(*state_of_train, sep=" ")

if count < len(state_of_train) and waiting_people == 0:
    print(f'The lift has empty spots!')
    print(*state_of_train, sep=" ")
