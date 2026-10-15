import spotify
import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

# songs = [
#     {
#         "title": "Blinding Lights",
#         "artist": "The Weeknd",
#         "duration": 200,
#         "plays": 5
#     },
#     {
#         "title": "Numb",
#         "artist": "Linkin Park",
#         "duration": 187,
#         "plays": 8
#     },
#     {
#         "title": "Shape of You",
#         "artist": "Ed Sheeran",
#         "duration": 234,
#         "plays": 3
#     }
# ]

songs = []

def main():
    while True:
        userChoice = input("====== SPOTIFY WRAPPED ======\n\n1. Add a song\n2. Record a listen\n3. Generate Spotify Wrapped\n4. Exit\n\nEnter your choice: ")
        userChoice = userChoice.strip()
        if userChoice == "1":
            newSong = spotify.add_song()
            songs.append(newSong)
        elif userChoice == "2":
            spotify.record_listen()
        elif userChoice == "3":
            spotify.generate_wrapped()
        elif userChoice == "4":
            messages.goodbye()
            break
        else:
            messages.invalidInput()

main()
