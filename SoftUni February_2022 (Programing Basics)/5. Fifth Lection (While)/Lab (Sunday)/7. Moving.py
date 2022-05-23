width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

whole_space = width_free_space * length_free_space * height_free_space
count_boxes = 0

while True:
    boxes = input()
    if boxes == "Done":
        break
    else:
        count_boxes += int(boxes)

    if count_boxes >= whole_space:
        break

diff = abs(whole_space - count_boxes)

if count_boxes < whole_space:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")