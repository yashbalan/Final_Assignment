def checkPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(checkPalindrome("madam"))
print(checkPalindrome("racecar"))
print(checkPalindrome("hello"))