start_of_interval = int(input())
end_of_interval = int(input())
magic_number = float(input())

combinations = 0
done = False
no_nums = False

for first in range(start_of_interval, end_of_interval + 1):
    for second in range(start_of_interval, end_of_interval + 1):
        combinations += 1
        if first + second == magic_number:
            print(f"Combination N:{combinations} ({first} + {second} = {first + second}) ")
            done = True
        if done:
            break
    if done:
        break

if not done:
    print(f"{combinations} combinations - neither equals {int(magic_number)}")