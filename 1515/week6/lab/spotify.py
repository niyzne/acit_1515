import messages
# ================================
# == LAB NOT DONE AT THE MOMENT ==
# ================================

# This file should define and implement the following functions:

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

def songDurationFunc(songDurationChoice):
    while True:
        if songDurationChoice == "1":
            songDurationMin = input("Enter duration (minutes): ")
            songDurationMin.strip()
            while True:
                if songDurationMin.isnumeric():
                    songDurationMin = int(songDurationMin)
                    break
                messages.invalidInput()
            songDurationSec = songDurationMin * 60
            return songDurationSec
        elif songDurationChoice == "2":
            songDurationSec = input("Enter duration (seconds): ")
            songDurationSec.strip()
            while True:
                if songDurationSec.isnumeric():
                    songDurationSec = int(songDurationSec)
                    break
                messages.invalidInput()
            return songDurationSec
        else:
            messages.invalidInput()

def totalSongs(songs):
    totalSongs = 0
    for i in songs:
        if "title" in i:
            totalSongs += 1

    return totalSongs

def totalPlays(songs):
    totalPlays = 0
    for dictionary in songs:
        if "plays" in dictionary:
            totalPlays += dictionary["plays"]

    return totalPlays

def totalListeningTimeInSec(songs):
    totalListeningTime = 0
    for dictionary in songs:
        if "duration" in dictionary:
            totalPlays += songs["duration"]

    return totalListeningTime

def mostPlayedSong(songs):
    most_plays = 0
    best_song = None

    for dictionary in songs:
        plays = dictionary["plays"]
        if plays > most_plays:
            most_plays = plays
            best_song = dictionary
    return most_plays, best_song

# def add_song
def add_song():
    songTitle = input("Enter song title: ")
    songArtist = input("Enter artist: ")
    songDurationChoice = input("Enter duration\n[1] minutes\n[2] seconds\nEnter mode: ")
    songDurationSec = songDurationFunc(songDurationChoice)
    songPlays = 0

    newSong = {"title":songTitle,"artist":songArtist,"duration":songDurationSec,"plays":songPlays}
    songs.append(newSong)

# def record_listen
def record_listen():
    if not songs:
        messages.songNotFound()
    else:
        songTitle = input("Enter song title: ")
        for song in songs:
            if songTitle == song["title"]:
                song["plays"] += 1
            messages.songNotFound()

# def generate_wrapped
def generate_wrapped():
    if songs:
        return f"""
        ========== YOUR SPOTIFY WRAPPED ==========

        Total Songs: {totalSongs(songs)}
        Total Plays: {totalPlays(songs)}
        Total Listening Time: {(totalListeningTimeInSec(songs)) / 60} minutes

        Your Most Played Song:
        {mostPlayedSong(songs)[1]["title"]} - {mostPlayedSong(songs)[1]["artist"]} ({mostPlayedSong(songs)[0]} plays)

        ==========================================
        """
    else:
        messages.songNotFound()

# ========== YOUR SPOTIFY WRAPPED ==========
#
# Total Songs: 3
# Total Plays: 16
# Total Listening Time: 52 minutes
#
# Your Most Played Song:
# Numb - Linkin Park (8 plays)
#
# ==========================================
