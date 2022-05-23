hour_exam = int(input()) * 60
minute_exam = int(input())
coming_hour = int(input()) * 60
coming_minute = int(input())

add_up_exam = hour_exam + minute_exam
add_up_coming = coming_hour + coming_minute

divide_exam_from_coming = abs(add_up_exam - add_up_coming)
minutes_passed = divide_exam_from_coming % 60
hours_passed = divide_exam_from_coming // 60

if add_up_coming > add_up_exam:
    print("Late")
    if divide_exam_from_coming > 59 and minutes_passed < 10:
        print(f"{hours_passed}:{minutes_passed:02d} hours after the start")
    elif divide_exam_from_coming > 59:
        print(f"{hours_passed}:{minutes_passed} hours after the start")
    else:
        print(f"{divide_exam_from_coming} minutes after the start")
elif add_up_coming == add_up_exam or divide_exam_from_coming in range(0, 31):
    print("On time")
    print(f"{minutes_passed} minutes before the start")
elif add_up_coming < add_up_exam and divide_exam_from_coming in range(31, 100000):
    print("Early")
    if divide_exam_from_coming > 59 and minutes_passed < 10:
        print(f"{hours_passed}:{minutes_passed:02d} hours before the start")
    elif divide_exam_from_coming > 59:
        print(f"{hours_passed}:{minutes_passed} hours before the start")
    else:
        print(f"{minutes_passed} minutes before the start")
