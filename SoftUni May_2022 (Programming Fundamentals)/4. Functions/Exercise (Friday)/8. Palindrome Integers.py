def is_palindrome(number):
    if number == number[::-1]:
        return True
    else:
        return False


numbers = input().split(", ")
for every_num in numbers:
    if is_palindrome(every_num):
        print('True')
    else:
        print('False')