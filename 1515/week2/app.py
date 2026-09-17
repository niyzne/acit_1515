school = "bcit"
statement = "is a cool school"

# string concatenation (joining together)
school_statement = school + statement

print(school)
print(statement)
print(school_statement)

# if we want actually space
school_statement = school + " " + statement
print(school_statement)

# or

statement = " is a cool school"
school_statement = school + statement
print(school_statement)

# You can also make a formatted string (fstirng)

school = "bcit"
statement = "is a cool school"

school_statement = f"{school} {statement}"
print(school_statement)

# or

school_statement = f"{school} really {statement}"
print(school_statement)
