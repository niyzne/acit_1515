colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

def invalidInput():
    print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')

def goodbye():
    print(f'{colors["blue"]}Have a good day{colors["reset"]}')
