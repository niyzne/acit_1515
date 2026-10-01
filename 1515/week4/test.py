year = 2026
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for month in range(12):
    for days in range(1, days_in_month[month] + 1):
        print(days)
