money_needed_for_vacation = float(input())
money_you_have = float(input())

all_days = 0
consecutive_days = 0
cant_save = False

while True:
    command = input()
    sum_command = float(input())

    all_days += 1

    if command == "spend":
        consecutive_days += 1
        money_you_have -= sum_command
        if money_you_have < 0:
            money_you_have = 0
        if consecutive_days == 5:
            cant_save = True
            break
    elif command == "save":
        consecutive_days = 0
        money_you_have += sum_command
        cant_save = False
        if money_you_have >= money_needed_for_vacation:
            break




if cant_save:
    print(f"You can't save the money.")
    print(f"{all_days}")
elif money_you_have >= money_needed_for_vacation:
    print(f"You saved the money for {all_days} days.")