def distChar(s1, s2):
    set1 = set(s1)
    set2 = set(s2)
    unique_chars = (set1 - set2) | (set2 - set1)
    return ''.join(sorted(unique_chars))

print(distChar('characters', 'alphabets'))
print(distChar('apples', 'oranges'))
print(distChar('apples', 'apples'))