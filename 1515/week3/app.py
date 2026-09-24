def times_by_ten(n):
    return n * 10


def odd_or_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

returnedValue = times_by_ten(5) # this then gets 'replaced' with 50, and that result can be used for other stuff
print(returnedValue)
odd_or_even(returnedValue)
