tasks = ['coding', 'dog', 'cat', 'movie']
tasks_upper = ['CODING', 'DOG', 'CAT', 'MOVIE']

give_tasks = ""
coffees = 0
extra_sleep = False

while give_tasks != "END":
    give_tasks = input()
    if give_tasks not in tasks and give_tasks not in tasks_upper:
        continue
    else:
        if give_tasks in tasks:
            coffees += 1
        elif give_tasks in tasks_upper:
            coffees += 2
    if coffees > 5:
        extra_sleep = True
        print(f'You need extra sleep')
        break

if not extra_sleep:
    print(coffees)


