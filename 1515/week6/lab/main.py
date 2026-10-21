import spotify
import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

def main():
    while True:
        userChoice = input("====== SPOTIFY WRAPPED ======\n\n1. Add a song\n2. Record a listen\n3. Generate Spotify Wrapped\n4. Exit\n\nEnter your choice: ")
        userChoice = userChoice.strip()
        if userChoice == "1":
            spotify.add_song()
        elif userChoice == "2":
            spotify.record_listen()
        elif userChoice == "3":
            spotify.generate_wrapped()
        elif userChoice == "4":
            messages.goodbye()
            break
            # exit() ?
        else:
            messages.invalidInput()

main()
