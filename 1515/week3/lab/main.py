# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================

import dow

def month_type(month):
    if isinstance(month, int):
        return dow.months_list[month - 1]

while True:
    user_choice = input("Hello friend. What do you want to do? Choices: [1] print all days in year, [2] print specific day, [q] quit: ")
    if user_choice == "1":
        dow.makeCalendar()
    elif user_choice == "2":
        year = int(input("Year: "))
        month = input("Month: ")
        if len(month) <= 2 and month.isnumeric():
            month = int(month)
            if month < 1 or month > 12:
                print("invalid month, try option 2 again")
                continue
            month = month_type(month)
        day = int(input("day (number): "))
        print(dow.getDayOfTheWeek(year, month, day))
        month = str(month)
    elif user_choice == "q":
        break
    else:
       print("Invalid choice, try again")

# ========================================
# == LAB NOT DONE AT THE CURRENT MOMENT ==
# ========================================
