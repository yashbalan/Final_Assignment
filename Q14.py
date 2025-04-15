def equivalent(str1, str2):
    max_len = 0
    result = ""

    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            substring = str1[i:j]
            doubled = substring * 2

            for k in range(len(substring)):
                rotated = doubled[k:k + len(substring)]
                if rotated in str2:
                    if len(substring) > max_len:
                        max_len = len(substring)
                        result = substring
                    elif len(substring) == max_len and substring < result:
                        result = substring
                    break

    return result

print(equivalent('hdjkou1', 'pokoudj'))
print(equivalent('ghajiop', 'abkoidj'))
print(equivalent('hdjkou1', 'pikpiaa'))
print(equivalent('abcd', 'cdab'))