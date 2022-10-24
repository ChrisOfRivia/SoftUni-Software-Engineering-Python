secret_message = input().split()


for word in secret_message:
    number = ''
    actual_word = ''
    whole_message = ''
    for character in word:
        if character.isdigit():
            number += character
        else:
            actual_word += character
    number = int(number)
    whole_message += chr(number)
    if len(actual_word) >= 2:
        whole_message += actual_word[-1] + actual_word[1:-1:] + actual_word[0]
    else:
        whole_message += actual_word
    print(whole_message, end=" ")
