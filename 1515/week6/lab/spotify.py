import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

# This file should define and implement the following functions:

def songDurationFunc(songDurationChoice):
    if songDurationChoice == "1":
        songDuration = int(input("Enter duration (minutes): "))
        songDurationSec = songDuration * 60
    elif songDurationChoice == "2":
        songDurationSec = int(input("Enter duration (seconds): "))
    else:
        messages.invalidInput()
    return songDurationSec

# def add_song
def add_song():
    songTitle = input("Enter song title: ")
    songArtist = input("Enter artist: ")
    songDurationChoice = input("Enter duration\n[1] minutes\n[2] seconds\nEnter mode: ")
    songDurationSec = songDurationFunc(songDurationChoice)
    songPlays = 0

    return {"title":songTitle,"artist":songArtist,"duration":songDurationSec,"plays":songPlays}

# def record_listen
def record_listen():
    songTitle = input("Enter song title: ")
    for song in songs:
        if songTitle == song["title"]:
            song["plays"] += 1
        messages.songNotFound()

# def generate_wrapped
def generate_wrapped():
    return f"========== YOUR SPOTIFY WRAPPED ==========\n\nTotal Songs: {len(students)}\nTotal Plays: {smth}\nTotal Listening Time: {smth} minutes\n\nYour Most Played Song:\n{song} - {artist} ({nuber of plays} plays)\n\n=========================================="
