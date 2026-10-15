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
    return songTitle, songArtist, songDuration

# def record_listen
def record_listen():
    pass
    songTitle = input("Enter song title: ")
    # Search through the list and increase the matching song's play count by 1.
    # If the song doesn't exist, display an error message.

# def generate_wrapped
def generate_wrapped():
    pass
    # return f"========== YOUR SPOTIFY WRAPPED ==========\n\nTotal Songs: {smth}\nTotal Plays: {smth}\nTotal Listening Time: {smth} minutes\n\nYour Most Played Song:\n{song} - {artist} ({nuber of plays} plays)\n\n=========================================="
