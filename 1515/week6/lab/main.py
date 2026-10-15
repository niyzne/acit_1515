# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

import spotify

songs = [
    {
        "title": "Blinding Lights",
        "artist": "The Weeknd",
        "duration": 200,
        "plays": 5
    },
    {
        "title": "Numb",
        "artist": "Linkin Park",
        "duration": 187,
        "plays": 8
    },
    {
        "title": "Shape of You",
        "artist": "Ed Sheeran",
        "duration": 234,
        "plays": 3
    }
]

# def main():
#     pass
#
# main()

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

while True:
    userChoice = input("====== SPOTIFY WRAPPED ======\n\n1. Add a song\n2. Record a listen\n3. Generate Spotify Wrapped\n4. Exit\n\nEnter your choice: ")
    userChoice = userChoice.strip()
    if userChoice == "1":
        pass
    elif userChoice == "2":
        pass
    elif userChoice == "3":
        pass
    elif userChoice == "4":
        goodbye()
        break
    else:
        invalidInput()
