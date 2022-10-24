strings = input().split(' ')
palindrome = input()

print([palindrome for palindrome in strings if palindrome[::-1] == palindrome])
print(f'Found palindrome {strings.count(palindrome)} times')