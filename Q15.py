def subPali(s):
    if not s:
        return 0

    n = len(s)
    max_len = 1

    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2

    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                if length > max_len:
                    max_len = length

    return max_len

print(subPali('bbbabcbabdfb'))
print(subPali('abcdefg'))
print(subPali('racecar'))
print(subPali('abba'))