# TODO: Breaking your code into functions
# TODO: using the return keyword effectively

def can_drive(age, has_license):
    if age >= 16:
        if has_license == True:
            return "You can drive"
    return "You cannot drive"

person_who_can_drive = can_drive(20, True)
person_who_cannot_drive = can_drive(21, False)

print(person_who_can_drive)
print(person_who_cannot_drive)
