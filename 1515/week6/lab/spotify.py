import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

# This file should define and implement the following functions:

def songDurationFunc(songDurationChoice):
    if songDurationChoice == "1":
        songDuration = int(input("Enter duration (minutes): "))
        songDuration = songDuration * 60
    elif songDurationChoice == "2":
        songDuration = int(input("Enter duration (seconds): "))
    else:
        messages.invalidInput()
    return songDuration

# def add_song
def add_song():
    songTitle = input("Enter song title: ")
    songArtist = input("Enter artist: ")
    songDurationChoice = input("Enter duration\n[1] minutes\n[2] seconds\nEnter mode: ")
    songDuration = songDurationFunc(songDurationChoice)

# Enter song title: Blinding Lights
# Enter artist: The Weeknd
# Enter duration (minutes): 3
# Enter duration (seconds): 20

# def record_listen
def record_listen():
    pass

# def generate_wrapped
def generate_wrapped():
    pass
