# A year is leap year if following conditions are satisfied
# 1) Year is multiple of 400
# 2) Year is multiple of 4 and not multiple of 100.

def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False
