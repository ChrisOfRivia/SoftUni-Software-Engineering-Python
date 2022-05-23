period = int(input())

doctors = 7
untreated_patients = 0
treated_patients = 0

for days in range(1, period + 1):
    if days % 3 == 0 and treated_patients < untreated_patients:
        doctors += 1
    patients_for_today = int(input())

    patients_left = doctors - patients_for_today
    if patients_for_today >= doctors:
        treated_patients += doctors
    elif patients_left in range(1, doctors):
        treated_patients += patients_for_today

    if patients_left < 0:
        untreated_patients += abs(patients_left)
    else:
        continue

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
