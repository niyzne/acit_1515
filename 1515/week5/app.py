# TODO: Breaking your code into functions
# TODO: using the return keyword effectively

def check_age(age):
    if age >= 18:
        return "Adult"
    return "Minor"

print(check_age(20)) # Adult
print(check_age(15)) # Minor
