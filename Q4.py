class UpperCaseException(Exception):
    pass

def evenIndexCapital(s):
    for char in s:
        if char.isupper():
            raise UpperCaseException("Input contains uppercase letters")

    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(chr(ord(s[i]) - 32) if 'a' <= s[i] <= 'z' else s[i])
        else:
            result.append(s[i])
    return ''.join(result)

print(evenIndexCapital('school'))
try:
    print(evenIndexCapital('School'))
except UpperCaseException as e:
    print(e)