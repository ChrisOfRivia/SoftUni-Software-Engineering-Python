vowels = ['a', 'o', 'u', 'e', 'i']

string = input()

print(*[x for x in string if x not in vowels], sep="")
