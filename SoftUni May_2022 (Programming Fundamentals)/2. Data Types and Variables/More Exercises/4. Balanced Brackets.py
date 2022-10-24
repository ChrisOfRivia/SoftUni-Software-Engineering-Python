lines = int(input())

some_list = []
opening =  0
balanced = 0
unbalanced = 0

for i in range(1, lines + 1):
    string = input()
    if string == "(" or string == ")":
        some_list.append(string)
        for index, symbol in enumerate(some_list):
            if symbol == ")":
                if some_list[index -1] == "(":
                    balanced += 1
                else:
                    unbalanced += 1
if balanced > 0 and unbalanced == 0:
    print("BALANCED")
else:
    print("UNBALANCED")