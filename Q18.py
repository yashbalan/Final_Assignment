def delDup(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(delDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))
print(delDup([-1, 1, -1, 8]))
print(delDup([1, 2, 3]))