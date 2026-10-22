import spotify
import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

mode = ["Add Song", "Record Listen", "Generate Wrapped"]

def main():
    while True:
       # userChoice = input("====== SPOTIFY WRAPPED ======\n\n1. Add a song\n2. Record a listen\n3. Generate Spotify Wrapped\n4. Exit\n\nEnter your choice: ")
        userChoice = input(f"""{messages.colors["yellow"]}====== SPOTIFY WRAPPED ======

1. Add a song
2. Record a listen
3. Generate Spotify Wrapped
4. Exit

Enter your choice: {messages.colors["reset"]}""")
        # print()
        # print(f"{messages.colors["yellow"]}============================={messages.colors["reset"]}")
        userChoice = userChoice.strip()
        if userChoice == "1":
            print(f"{messages.colors["green"]}you have chosen mode {mode[0]}{messages.colors["reset"]}")
            spotify.add_song()
        elif userChoice == "2":
            print(f"{messages.colors["green"]}you have chosen mode {mode[1]}{messages.colors["reset"]}")
            spotify.record_listen()
        elif userChoice == "3":
            print(f"{messages.colors["green"]}you have chosen mode {mode[2]}{messages.colors["reset"]}")
            spotify.generate_wrapped()
        elif userChoice == "4":
            messages.goodbye()
            break
            # exit() ?
        else:
            messages.invalidInput()

main()
