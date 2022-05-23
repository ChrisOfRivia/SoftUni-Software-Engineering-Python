from math import floor

needed_hours = int(input())
days_the_firm_has = int(input())
workers = int(input())

workers_on_study = days_the_firm_has - (days_the_firm_has * 0.10)

work_hours = workers_on_study * 8

hours_workers_work = workers * (2 * days_the_firm_has)

all_hours = floor(work_hours + hours_workers_work)

diff = abs(all_hours - needed_hours)

if all_hours >= needed_hours:
    print(f"Yes!{diff} hours left.")
else:
    print(f"Not enough time!{diff} hours needed.")