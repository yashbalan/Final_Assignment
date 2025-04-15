from collections import Counter


def check(s, k):
    if k == 0:
        counts = Counter(s)
        if len(set(counts.values())) == 1:
            return s
        return ''

    n = len(s)
    if k >= n:
        return ''

    counts = Counter(s)

    for target in range(max(counts.values()), 0, -1):
        removal_needed = 0
        possible = True

        for char, cnt in counts.items():
            if cnt > target:
                removal_needed += (cnt - target)
            elif cnt < target:
                possible = False
                break

        if possible and removal_needed <= k:
            result = []
            remaining = k - removal_needed
            temp_counts = counts.copy()

            for char in s:
                if temp_counts[char] > target and remaining > 0:
                    remaining -= 1
                    temp_counts[char] -= 1
                else:
                    if temp_counts[char] > 0:
                        result.append(char)
                        temp_counts[char] -= 1

            return ''.join(result)

    return ''

print(check('aabbcc', 0))
print(check('aabbbcc', 0))
print(check('aabbbcc', 1))
print(check('aabbbcc', 2))
print(check('aabbbcc', 3))
print(check('aabbbcc', 4))
print(check('aabbbcc', 5))
print(check('aabbbcc', 6))
print(check('aabbbcc', 7))
print(check('aaaabbcc', 4))