class InvalidRollException(Exception):
    pass


def fee(base_fee, roll):
    if len(roll) != 7:
        raise InvalidRollException("Roll number must be 7 characters long")

    dept = roll[:2]
    if dept not in {'DS', 'CS', 'EE', 'ME'}:
        raise InvalidRollException("Invalid department code")

    try:
        year = int(roll[2:4])
    except ValueError:
        raise InvalidRollException("Invalid year in roll number")

    program = roll[4]
    if program not in {'1', '2'}:
        raise InvalidRollException("Invalid program code")

    duration = 4 if program == '1' else 2
    current_year = 22  # 2022

    if year > current_year:
        raise InvalidRollException("Admission year cannot be in the future")

    total_years = min(duration, current_year - year + 1)

    total_fee = 0
    current_fee = base_fee
    for _ in range(total_years):
        total_fee += current_fee
        current_fee = int(current_fee * 1.1)

    return total_fee


# Test cases
print(fee(100000, 'CS20143'))
print(fee(100000, 'DS18243'))
try:
    print(fee(100000, 'EEL6243'))
except InvalidRollException as e:
    print(e)