def fibonacci_sequence(number):
    queue_nums = []

    for i in range(number):
        if i == 0:
            queue_nums.append(0)
        elif i == 1:
            queue_nums.append(1)
        else:
            queue_nums.append(queue_nums[i - 2] + queue_nums[i - 1])

    return  queue_nums
