import spotify
import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

def main():
    while True:
        userChoice = input(f"""{messages.colors["white"]}====== SPOTIFY WRAPPED ======

[1] Add a song
[2] Record a listen
[3] Generate Spotify Wrapped

[q] Exit

Enter your choice: {messages.colors["reset"]}""")
        userChoice = userChoice.strip()
        if userChoice == "1":
            spotify.add_song()
        elif userChoice == "2":
            spotify.record_listen()
        elif userChoice == "3":
            spotify.generate_wrapped()
        elif userChoice == "q":
            messages.goodbye()
            break
        else:
            messages.invalidInput()

main()
