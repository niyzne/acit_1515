# Lesson Summary

# =============
# == STRINGS ==
# =============

# Starting with strings

print("this is bcit and it's a cool school")

# OR

print('this is bcit and it\'s a cool school')

# ------------------------------------
# -- Quotation marks inside strings --
# ------------------------------------

print("He said: \"what a cool school bcit is\"")

# OR

print('He said: "what a cool school bcit is"')

# ----------------------------------
# -- Storing strings in variables --
# ----------------------------------

# Instead of typing the same thing multiple times,

# we can store it in a variable.

statement = "bcit is a cool school"
print(statement)

# You can also modify the statement.

statement = "bcit is alright"
print(statement)

# --------------------
# -- Variable names --
# --------------------

school_statement = "bcit is a very cool school"
print(school_statement)

# You can write spaces in strings,
# but you can't have spaces in variable names.
# Use _ instead.

# ==========================
# == STRING CONCATENATION ==
# ==========================

school = "bcit"
statement = "is a cool school"

# String concatenation means joining strings together.

school_statement = school + statement

print(school)
print(statement)
print(school_statement)

# --------------------
# -- Adding a space --
# --------------------

school_statement = school + " " + statement
print(school_statement)

# OR

statement = " is a cool school"
school_statement = school + statement
print(school_statement)

# ===============
# == F-STRINGS ==
# ===============

school = "bcit"
statement = "is a cool school"

school_statement = f"{school} {statement}"
print(school_statement)

# You can also add other words inside an f-string.

school_statement = f"{school} really {statement}"
print(school_statement)

# =============
# == NUMBERS ==
# =============

younger_brother_age = 19
older_sister_age = 20

print(younger_brother_age + older_sister_age)

# Numbers are written without quotes.

# ==========================
# == CHECKING DATA TYPES ==
# ==========================

# You can find out what type of data you're working with.
print(type(younger_brother_age))

# Putting a number inside quotes makes it a string.
younger_brother_age = "19"
print(type(younger_brother_age))

# =====================
# == PRINT AND INPUT ==
# =====================

# This program figures out your age.

current_year = 2026

# print() simply prints something.
print("Tell me your birth year: ")

# input() prints and allows the user to input something.
input("Tell me your birth year: ")

# ==========================
# == CALCULATING YOUR AGE ==
# ==========================

current_year = 2026

birth_year = int(input("Tell me your birth year: "))

print(type(current_year))
print(type(birth_year))

print(current_year - birth_year)

# You could also convert the input later.

birth_year = input("Tell me your birth year: ")

print(type(current_year))
print(type(birth_year))

print(current_year - int(birth_year))
