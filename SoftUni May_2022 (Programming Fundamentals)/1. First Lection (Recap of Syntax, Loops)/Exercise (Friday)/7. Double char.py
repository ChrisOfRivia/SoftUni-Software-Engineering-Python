string = ""

while string != "End":
    string = input()

    if string == "End":
        break
    if string == "SoftUni":
        continue
    else:
        for chars in string:
            print(chars * 2, end="")
        print("")


