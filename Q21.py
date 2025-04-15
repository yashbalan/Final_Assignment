def moveZeros(lst):
    return [x for x in lst if x != 0] + [x for x in lst if x == 0]

print(moveZeros([1, 2, 0, 4, 0, 5, 0]))
print(moveZeros([0, 1, 0, 3, 12]))
print(moveZeros([0, 0, 0, 1]))
print(moveZeros([1, 2, 3]))