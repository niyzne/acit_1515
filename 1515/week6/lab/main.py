import spotify
import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

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

def main():
    while True:
        userChoice = input("====== SPOTIFY WRAPPED ======\n\n1. Add a song\n2. Record a listen\n3. Generate Spotify Wrapped\n4. Exit\n\nEnter your choice: ")
        userChoice = userChoice.strip()
        if userChoice == "1":
            spotify.add_song()
        elif userChoice == "2":
            pass
        elif userChoice == "3":
            pass
        elif userChoice == "4":
            messages.goodbye()
            break
        else:
            messages.invalidInput()

main()
