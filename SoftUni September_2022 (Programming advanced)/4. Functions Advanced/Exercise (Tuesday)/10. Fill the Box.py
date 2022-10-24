def fill_the_box(height, length, width, *args):
    size_box = height * length * width
    first_lesser_num = True

    nums_left = []

    for nums in args:
        if nums == 'Finish':
            if size_box > 0:
                return f"There is free space in the box. You could put {size_box} more cubes."
            else:
                return f"No more free space! You have {sum(nums_left)} more cubes."

        if nums > size_box:
            nums -= size_box
            size_box = 0
            nums_left.append(nums)
        else:
            size_box -= nums
