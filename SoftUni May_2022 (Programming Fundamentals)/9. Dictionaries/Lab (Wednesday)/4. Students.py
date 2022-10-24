programming_basics = {}
fundamentals = {}
advanced = {}

students_list = input()

while True:
    if students_list == 'fundamentals' or students_list == 'advanced' or students_list == 'programming_basics':
        break
    else:
        split = students_list.split(":")

    student = split[0]
    id = int(split[1])
    course = split[2]

    if course == 'programming basics':
        if student not in programming_basics:
            programming_basics[student] = id
        else:
            programming_basics[student] += id
    elif course == 'fundamentals':
        if student not in fundamentals:
            fundamentals[student] = id
        else:
            fundamentals[student] += id
    elif course == 'advanced':
        if student not in advanced:
            advanced[student] = id
        else:
            advanced[student] += id

    students_list = input()

if students_list == 'fundamentals':
    for i in fundamentals:
        print(f'{i} - {fundamentals.get(i)}')
elif students_list == 'programming_basics':
    for i in programming_basics:
        print(f'{i} - {programming_basics.get(i)}')
elif students_list == 'advanced':
    for i in advanced:
        print(f'{i} - {advanced.get(i)}')
