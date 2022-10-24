chr_str1 = 0

num1 = 0
num2 = 0

sum = 0

strings = input().split(" ")

str1 = strings[0]
str2 = strings[1]

if len(str1) > len(str2):
    for i in range(len(str1)):
        num1 = 0
        num2 = 0
        for j in range(len(str1)):
            try:
                num1 = ord(str1[i])
                break
            except IndexError:
                pass

        for k in range(len(str2)):
            try:
                num2 = ord(str2[i])
                break
            except IndexError:
                pass

        if num1 != 0 and num2 != 0:
            sum += num1 * num2
        elif num1 == 0:
            sum += num2
        elif num2 == 0:
            sum += num1
        else:
            pass
else:
    for i in range(len(str2)):
        num1 = 0
        num2 = 0
        for j in range(len(str1)):
            try:
                num1 = ord(str1[i])
                break
            except IndexError:
                pass

        for k in range(len(str2)):
            try:
                num2 = ord(str2[i])
                break
            except IndexError:
                pass

        if num1 != 0 and num2 != 0:
            sum += num1 * num2
        elif num1 == 0:
            sum += num2
        elif num2 == 0:
            sum += num1
        else:
            pass

print(sum)