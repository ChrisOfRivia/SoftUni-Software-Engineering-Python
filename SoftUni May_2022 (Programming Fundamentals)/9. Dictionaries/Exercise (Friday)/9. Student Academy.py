n = int(input())

grades_dict = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in grades_dict:
        grades_dict[name] = []
    grades_dict[name].append(grade)

for student, grade in grades_dict.items():
    if sum(grade) / len(grade) < 4.50:
        pass
    else:
        print(f'{student} -> {sum(grade) / len(grade):.2f}')
