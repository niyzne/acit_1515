colors = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "reset": "\033[0m"
}

# bad (red)

def invalidInput():
    print(f'{colors["red"]}Invalid input, try again{colors["reset"]}')

def songNotFound():
    print(f'{colors["red"]}404 - Song Not Found{colors["reset"]}')

def songNotFound():
    print(f'{colors["red"]}404 - Song library not found{colors["reset"]}')

# statement (blue)

def goodbye():
    print(f'{colors["blue"]}Have a good day{colors["reset"]}')

# success (green)

def songRecorded():
    print(f'{colors["green"]}Song has been recorded{colors["reset"]}')
