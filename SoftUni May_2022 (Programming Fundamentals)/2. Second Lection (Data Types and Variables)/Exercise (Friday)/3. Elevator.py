people = int(input())
capacity = int(input())

one_course = 0
courses = 0

while people > 0:
    if people - capacity < 0:
        people -= capacity
        courses += 1
    else:
        people -= capacity
        courses += 1
print(courses)