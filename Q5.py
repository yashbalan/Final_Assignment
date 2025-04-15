def shift(s, count=0, account=0):
    if count < 0 or account < 0:
        raise ValueError("count and account must be non-negative")

    if not s:
        return s

    n = len(s)
    account = account % n
    rotated_left = s[account:] + s[:account]

    count = count % n
    rotated_right = rotated_left[-count:] + rotated_left[:-count]

    return rotated_right


print(shift('NinjaHattori'))
print(shift('NinjaHattori', account=3))
print(shift('NinjaHattori', count=3))
print(shift('NinjaHattori', count=3, account=3))
print(shift('NinjaHattori', account=3, count=6))
print(shift('NinjaHattori', account=6, count=3))