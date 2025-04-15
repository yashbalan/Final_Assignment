def delVowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ''.join([c for c in s if c not in vowels])

print(delVowels('SfgEtfjofubjiekp'))
print(delVowels('aElOu'))
print(delVowels('Python Programming'))