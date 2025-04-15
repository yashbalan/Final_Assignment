def minIndexFirstString(str1, str2):
    max_index = -1
    for i in range(len(str1)):
        if str1[i] in str2 and i > max_index:
            max_index = i
    return max_index

print(minIndexFirstString('tiger', 'integer'))
print(minIndexFirstString('integer', 'tiger'))
print(minIndexFirstString('apple', 'orange'))