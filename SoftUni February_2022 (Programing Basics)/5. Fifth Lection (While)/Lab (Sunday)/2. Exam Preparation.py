number_bad_grades = int(input())

bad_grade = 0
problems_counter = 0
grade_counter = 0
grade_sum = 0
last_problem = ""
done = False
need_break = False

while True:
    name_of_problem = input()
    if name_of_problem == "Enough":
        done = True
        break
    grade = int(input())

    problems_counter += 1
    grade_counter += 1
    grade_sum += grade

    last_problem = name_of_problem

    if grade <= 4:
        bad_grade += 1
        if bad_grade >= number_bad_grades:
            need_break = True
            break

if done:
    average_score = grade_sum / grade_counter
    print(f"Average score: {average_score:.2f}")
    print(f"Number of problems: {problems_counter}")
    print(f"Last problem: {last_problem}")

elif need_break:
    print(f"You need a break, {bad_grade} poor grades.")