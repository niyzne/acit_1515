# figure out if a num is odd or even
# use input() to get a num
# show the user a warning if they don't enter a number
num = input("Enter a number: ")

if num.isnumeric():
    num = int(num)
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Please enter a number")

# we want to rerun the thing, but how do we do it without, repasting the code (loops im guessing)
num2 = input("Enter another number: ")
