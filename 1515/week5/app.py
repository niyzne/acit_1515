# TODO: Breaking your code into functions
# TODO: using the return keyword effectively

def check_age(age):
    return age >= 16

def can_drive(age, has_license):
    if check_age(age) and has_license:
        return "You can drive"
    return "You cannot drive"

person_who_can_drive = can_drive(20, True)
person_who_cannot_drive = can_drive(21, False)

print(person_who_can_drive)
print(person_who_cannot_drive)
