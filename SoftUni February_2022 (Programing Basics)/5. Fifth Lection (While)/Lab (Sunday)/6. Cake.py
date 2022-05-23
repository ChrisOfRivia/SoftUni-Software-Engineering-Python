width_cake = int(input())
length_cake = int(input())

whole_cake = width_cake * length_cake
all_pieces = 0
no_more_cake = False

while True:
    pieces = input()

    if pieces == "STOP":
        break
    all_pieces += int(pieces)
    whole_cake -= int(pieces)
    if whole_cake <= 0:
        no_more_cake = True
        break

if no_more_cake:
    print(f"No more cake left! You need {abs(whole_cake)} pieces more.")
else:
    print(f"{whole_cake} pieces are left.")