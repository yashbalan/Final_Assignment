class DimensionMismatchException(Exception):
    pass

def matMul(mat1, mat2):
    n1 = int(len(mat1) ** 0.5)
    n2 = int(len(mat2) ** 0.5)

    if n1 * n1 != len(mat1) or n2 * n2 != len(mat2) or n1 != n2:
        raise DimensionMismatchException("Matrices must be square and of same dimension")

    n = n1
    result = []

    for i in range(n):
        for j in range(n):
            val = 0
            for k in range(n):
                val += mat1[i * n + k] * mat2[k * n + j]
            result.append(val)

    return result

print("Testing matMul:")
try:
    print(matMul([1, 2, 0, 4, 0, 5, 0, 7, 9], [1, 2, 0, 4, 0, 5, 0, 7, 9]))
except DimensionMismatchException as e:
    print(e)

try:
    print(matMul([1, 2, 3, 4], [1, 2, 3, 4]))
except DimensionMismatchException as e:
    print(e)

try:
    print(matMul([1, 2, 3], [1, 2, 3, 4]))
except DimensionMismatchException as e:
    print(e)