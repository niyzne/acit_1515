# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================

# dictionaries and functions

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
days_of_week = {
    0: "Saturday",
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday"
}
months_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Part 1

def isLeapYear(year):
    return (year % 400 == 0) or (year % 4 == 0 and not year % 100 == 0)

def getDayOfTheWeek(year, month, day):
    # step 1
    last_two_digits = str(year)[2:]
    number_of_12s = int(last_two_digits) // 12

    # step 2
    remainder = int(last_two_digits) % 12

    # step 3
    number_of_4s = remainder // 4

    # step 4
    day_of_month = day

    # step 5
    month_code = months[month[:3].capitalize()] + century[str(year)[:2]]

    if (month[:3].capitalize() == "Jan" or month[:3].capitalize() == "Feb") and isLeapYear(year):
        month_code -= 1

    # step 6
    day_of_week = (number_of_12s + remainder + number_of_4s + day_of_month + month_code) % 7
    day = days_of_week[day_of_week]
    return day

# Part 2

def makeCalendar():
    for month in range(len(months_list)):
        for day in range(1, days_in_month[month] + 1):
            day_of_week = getDayOfTheWeek(2026, months_list[month], day)
            print(f"{month + 1}-{day}-2026 is a {day_of_week}")

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
