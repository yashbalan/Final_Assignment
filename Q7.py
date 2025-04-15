class InvalidInputException(Exception):
    pass


def change(s):
    if not all(c in {'R', 'G'} for c in s):
        raise InvalidInputException("String must contain only 'R' and 'G'")

    count_r = s.count('R')
    count_g = len(s) - count_r
    return min(count_r, count_g)

print(change('R'))
print(change('RGRGR'))
print(change('GRG'))
try:
    print(change('RGB'))
except InvalidInputException as e:
    print(e)