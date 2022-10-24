def chars_in_between(first_char, second_char):
    for between in range(ord(first_char) + 1, ord(second_char)):
        print(chr(between), end=" ")


first_string = input()
second_string = input()

chars_in_between(first_string, second_string)