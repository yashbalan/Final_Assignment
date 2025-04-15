def extractDup(lst):
    seen = set()
    duplicates = set()

    for num in lst:
        if num in seen and num not in duplicates:
            duplicates.add(num)
        seen.add(num)

    return sorted(duplicates)

print(extractDup([10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]))
print(extractDup([-1, 1, -1, 8]))
print(extractDup([-3, 1, -1, 8]))