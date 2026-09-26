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
    #return number_of_12s
    #print(number_of_12s)

    # step 2
    remainder = int(last_two_digits) % 12
    #return remainder
    #print(remainder)

    # step 3
    number_of_4s = remainder // 4
    #return number_of_4s
    #print(number_of_4s)

    # step 4
    day_of_month = day

    # step 5
    months = {
        "Jan": 1,
        "Feb": 4,
        "Mar": 4,
        "Apr": 0,
        "May": 2,
        "Jun": 5,
        "Jul": 0,
        "Aug": 3,
        "Sep": 6,
        "Oct": 1,
        "Nov": 4,
        "Dec": 6
    }
    century = {
        "16": 6,
        "17": 4,
        "18": 2,
        "19": 0,
        "20": 6,
        "21": 4
    }
    month_code = months[month[:3].capitalize()] + century[str(year)[:2]]
    #return month_code

    # step 6
    day_of_week = (number_of_12s + remainder + number_of_4s + day_of_month + month_code) % 7

# Part 2

def makeCalendar():
    pass

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
