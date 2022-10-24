schedule = input().split(", ")

while True:
    try:
        command = input()
        if command == 'course start':
            break
        command = command.split(":")
        task = command[0]
        lesson_title = command[1]
        if task == 'Add':
            if lesson_title not in schedule:
                schedule.append(lesson_title)
            else:
                continue
        elif task == 'Insert':
            if lesson_title not in schedule:
                index = command[2]
                index = int(index)
                schedule.insert(index, lesson_title)
            else:
                continue
        elif task == 'Remove':
            if lesson_title in schedule:
                schedule.remove(lesson_title)
            else:
                continue
            if f'{lesson_title}-Exercise' in schedule:
                schedule.remove(f'{lesson_title}-Exercise')
        elif task == 'Swap':
            swap_with = command[2]
            index_first = schedule.index(lesson_title)
            index_second = schedule.index(swap_with)
            if lesson_title in schedule and swap_with in schedule:
                schedule[index_first], schedule[index_second] = schedule[index_second], schedule[index_first]
            else:
                continue
            if f'{lesson_title}-Exercise' in schedule:
                schedule.remove(f'{lesson_title}-Exercise')
                schedule.insert(index_second + 1, f'{lesson_title}-Exercise')
            elif f'{swap_with}-Exercise' in schedule:
                schedule.remove(f'{swap_with}-Exercise')
                schedule.insert(index_first + 1, f'{swap_with}-Exercise')
        elif task == 'Exercise':
            if f'{lesson_title}-Exercise' in schedule:
                continue
            if lesson_title not in schedule:
                schedule.append(lesson_title)
                index_lesson_title = schedule.index(lesson_title)
                schedule.insert(index_lesson_title + 1, f'{lesson_title}-{task}')
            elif lesson_title in schedule:
                index_lesson_title = schedule.index(lesson_title)
                schedule.insert(index_lesson_title + 1, f'{lesson_title}-{task}')
    except EOFError:
        pass


for num_task, task in enumerate(schedule):
    num_task += 1
    result = f'{num_task}.{task}'
    print(result)
