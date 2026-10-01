def is_leap_year(year_input):
    return True

year = 2024
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if is_leap_year(year):
    days_in_month[1] = 29

for month in range(len(days_in_month)):
    for day in range(1, days_in_month[month] + 1):
        print(f"{month + 1}-{day}-{year}")
