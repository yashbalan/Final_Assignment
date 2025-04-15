class LengthMismatchException(Exception):
    pass

def weave(list1, list2):
    if len(list1) != len(list2):
        raise LengthMismatchException("Lists must be of equal length")
    return [x for pair in zip(list1, list2) for x in pair]

print(weave([], []))
print(weave([1, 2, 3], [4, 5, 6]))
try:
    print(weave([1, 2], [3]))
except LengthMismatchException as e:
    print(e)