def firstLetters(s):
    result = []
    in_word = False
    for char in s:
        if char != ' ' and not in_word:
            result.append(char)
            in_word = True
        elif char == ' ':
            in_word = False
    return ''.join(result)

print(firstLetters('bad is nice'))
print(firstLetters('hello other world'))
print(firstLetters('  extra  spaces  '))