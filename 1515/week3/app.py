# figure out if a num is odd or even
# use input() to get a num
# show the user a warning if they don't enter a number

# def odd_or_even(n):
#     if n.isnumeric():
#         n = int(n)
#         if n % 2 == 0:
#             return "Even"
#         return "Odd"
#     return "Please enter a number"
#
# num = input("Enter a number: ")
# print(odd_or_even(num))

def odd_or_even(n):
    if n.isnumeric():
        n = int(n)
        if n % 2 == 0:
            print("Even")
        else:
            print("Odd")
    else:
        print("Please enter a number")

num = input("Enter a number: ")
odd_or_even(num)
