# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================

import dow

while True:
    user_choice = input("Hello friend. What do you want to do? Choices: [1] print all days in year, [2] print specific day, [*] quit: ")
    if user_choice == "1":
        dow.makeCalendar()
    if user_choice == "2":
        year = int(input("Year: "))
        month = input("Month (name): ")
        day = int(input("day (number): "))
        dow.getDayOfTheWeek(year, month, day)
    break

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
