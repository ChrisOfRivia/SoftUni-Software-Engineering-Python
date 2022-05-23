name_of_student = input()

bad_grade = 0
average_grade = 0
school_class = 0
grade = 0
expelled = False

while school_class < 12:
    grade = float(input())

    if grade < 4.00:
        bad_grade += 1
        if bad_grade > 1:
            expelled = True
            school_class += 1
            break
    else:
        average_grade += grade
        school_class += 1

if expelled:
    print(f"{name_of_student} has been excluded at {school_class} grade")
else:
    average_grade /= school_class
    print(f"{name_of_student} graduated. Average grade: {average_grade:.2f}")
