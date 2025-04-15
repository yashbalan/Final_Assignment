def oddCollatz(n):
    sequence = []
    while n != 1:
        if n % 2 != 0:
            sequence.append(n)
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    sequence.append(1)
    return sequence

print(oddCollatz(1))
print(oddCollatz(3))
print(oddCollatz(5))
print(oddCollatz(7))
print(oddCollatz(12))