num_students = int(input())

dict_students = {}

for each_student in range(num_students):
    name, grade = input().split(" ")
    if name not in dict_students:
        dict_students[name] = []
    dict_students[name].append(float(grade))

for student_name, student_grades in dict_students.items():
    str_grades = [str(f"{grade:.2f}") for grade in student_grades]
    print(f'{student_name} -> {" ".join(str_grades)} (avg: {(sum(student_grades) / len(student_grades)):.2f})')