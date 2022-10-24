def palindrome(word, index):
    result = ''

    if word == word[::-1]:
        result += f"{word} is a palindrome"
    else:
        result += f"{word} is not a palindrome"

    return result

print(palindrome("abcba", 0))
