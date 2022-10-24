all_courses = {}

while True:
    course_and_student = input()
    if course_and_student == 'end':
        break
    course, student = course_and_student.split(" : ")

    if course not in all_courses:
        all_courses[course] = [student]
    elif course in all_courses and student not in all_courses[course]:
        all_courses[course].append(student)

for course in all_courses:
    print(f'{course}: {len(all_courses[course])}')
    for students in all_courses[course]:
        print(f'-- {students}')
