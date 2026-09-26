# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================

# Part 1

def isLeapYear(year):
    if (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0):
        return True
    return False

def getDayOfTheWeek(year, month, day):
    # step 1
    last_two_digits = str(year)[2:]
    number_of_12s = int(last_two_digits) // 12
    return number_of_12s

# Part 2

def makeCalendar():
    pass

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
