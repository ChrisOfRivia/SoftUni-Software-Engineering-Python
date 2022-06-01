year = int(input())

happy_year = False

while not happy_year:
    year += 1
    set_year = set()
    for index in range(len(str(year))):
        set_year.add(str(year)[index])
    happy_year = len(str(year)) == len(set_year)
print(year)
