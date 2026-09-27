# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================

import dow

while True:
    user_choice = input("Hello friend. What do you want to do? Choices: [1] print all days in year, [2] print specific day, [q] quit: ")
    if user_choice == "1":
        dow.makeCalendar()
    elif user_choice == "2":
        year = int(input("Year: "))
        month = input("Month (name): ")
        day = int(input("day (number): "))
        print(dow.getDayOfTheWeek(year, month, day))
    elif user_choice == "q":
        break
    else:
       print("Invalid choice, try again")

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
