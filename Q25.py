def kMax(lst, k):
    if k <= 0 or k > len(lst):
        raise ValueError("k must be between 1 and length of list")

    unique = list(set(lst))
    unique.sort(reverse=True)
    return unique[k - 1]

print(kMax([10, 2, 4, 5, 7, 9], 1))
print(kMax([10, 2, 4, 5, 7, 9], 2))
print(kMax([10, 2, 4, 5, 7, 9], 3))
try:
    print(kMax([1, 2, 3], 4))
except ValueError as e:
    print(e)