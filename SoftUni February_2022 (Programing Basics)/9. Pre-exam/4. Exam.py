number_students = int(input())

all_grades = 0
num_grades = 0
excellent = 0
good = 0
medium = 0
bad = 0

for each_student in range(number_students):
    grade = float(input())
    num_grades += 1
    all_grades += grade

    if 2.00 <= grade <= 2.99:
        bad += 1

    elif 3.00 <= grade <= 3.99:
        medium += 1

    elif 4.00 <= grade <= 4.99:
        good += 1

    elif grade >= 5.00:
        excellent += 1

percent_excellent = excellent / num_grades * 100
percent_good = good / num_grades * 100
percent_medium = medium / num_grades * 100
percent_bad = bad / num_grades * 100

all_grades_percent = all_grades / number_students

print(f"Top students: {percent_excellent:.2f}%")
print(f"Between 4.00 and 4.99: {percent_good:.2f}%")
print(f"Between 3.00 and 3.99: {percent_medium:.2f}%")
print(f"Fail: {percent_bad:.2f}%")
print(f"Average: {all_grades_percent:.2f}")
