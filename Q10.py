def separate(s):
    if not s:
        return []

    result = []
    current = s[0]

    for char in s[1:]:
        if char == current[-1]:
            current += char
        else:
            result.append(current)
            current = char
    result.append(current)

    return result

print(separate('cartoon'))
print(separate('network'))
print(separate('aabbcc'))
print(separate('cccbbaaa'))