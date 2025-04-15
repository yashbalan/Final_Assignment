class DimensionMismatchException(Exception):
    pass


def printMat(lst):
    n = len(lst)
    sqrt_n = int(n ** 0.5)
    if sqrt_n * sqrt_n != n:
        raise DimensionMismatchException("List length must be a perfect square")

    for i in range(sqrt_n):
        print(' '.join(map(str, lst[i * sqrt_n:(i + 1) * sqrt_n])))

print("Testing printMat:")
try:
    printMat([1, 2, 0, 4, 0, 5, 0, 7, 9])
except DimensionMismatchException as e:
    print(e)

try:
    printMat([1, 2, 3, 4])
except DimensionMismatchException as e:
    print(e)

try:
    printMat([1, 2, 3])
except DimensionMismatchException as e:
    print(e)