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

lowercase_words = ["a", "an", "the", "and", "but", "or", "as", "at", "by", "for", "in", "of", "on", "to", "vs"]

mode = ["Add Song", "Record Listen", "Generate Wrapped"]

def songDurationFunc(songDurationChoice):
    while True:
        if songDurationChoice == "1":

            songDurationMin = input("Enter duration (minutes): ")
            songDurationMin.strip()
            while True:
                if songDurationMin.isnumeric():
                    songDurationMin = int(songDurationMin)
                    break
                else:
                    messages.invalidInput()
                    return
            songDurationSec = songDurationMin * 60
            return songDurationSec

        elif songDurationChoice == "2":
            songDurationSec = input("Enter duration (seconds): ")
            songDurationSec.strip()
            while True:
                if songDurationSec.isnumeric():
                    songDurationSec = int(songDurationSec)
                    break
                else:
                    messages.invalidInput()
                    return
            return songDurationSec

        elif songDurationChoice == "3":
            songDurationInMin = input("Enter duration (minutes): ")
            songDurationInMin.strip()
            while True:
                if songDurationInMin.isnumeric():
                    songDurationInMin = int(songDurationInMin)
                    break
                else:
                    messages.invalidInput()
                    return
            songDurationInSecPart1 = songDurationInMin * 60

            songDurationInSec = input("Enter duration (seconds): ")
            songDurationInSec.strip()
            while True:
                if songDurationInSec.isnumeric():
                    songDurationInSec = int(songDurationInSec)
                    break
                else:
                    messages.invalidInput()
                    return
            songDurationInSecPart2 = songDurationInSec
            songDurationSec = songDurationInSecPart1 + songDurationInSecPart2
            return songDurationSec

        else:
            messages.invalidInput()
            return

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
            totalListeningTime += dictionary["duration"]

    return totalListeningTime

def mostPlayedSong(songs):
    most_plays = 0
    best_song = None

    for dictionary in songs:
        plays = dictionary["plays"]
        if plays >= most_plays:
            most_plays = plays
            best_song = dictionary
    return most_plays, best_song

def titling(words):
    wordList = words.split()
    newString = []
    for word in wordList:
        if word in lowercase_words:
            newString.append(word)
        else:
            if isinstance(word, str):
                newString.append(word.capitalize())
            else:
                newString.append(word)

    return " ".join(newString)

# def add_song
def add_song():
    print(f"{messages.colors["green"]}Mode Selected: {mode[0]}{messages.colors["reset"]}")

    songTitle = input("Enter song title: ")
    songTitle.strip().lower()
    songTitle = titling(songTitle)

    songArtist = input("Enter artist: ")
    songArtist.strip().lower()
    songArtist = titling(songArtist)

    while True:
        songDurationChoice = input("Enter duration\n[1] minutes\n[2] seconds\n[3] minutes and seconds\nEnter mode: ")
        if songDurationChoice == "1" or songDurationChoice == "2" or songDurationChoice == "3":
            songDurationSec = songDurationFunc(songDurationChoice)
            break
        else:
            messages.invalidInput()

    songPlays = 0
    print(f"""{messages.colors["green"]}======= Song Added =======

Song: {songTitle}
Artist: {songArtist}
Song Duration: {(songDurationSec / 60):.2f} minutes

==========================={messages.colors["reset"]}""")

    newSong = {"title":songTitle,"artist":songArtist,"duration":songDurationSec,"plays":songPlays}
    songs.append(newSong)

# def record_listen
def record_listen():
    if not songs:
        messages.songLibraryNotFound()
    else:
        print(f"{messages.colors["green"]}Mode Selected: {mode[1]}{messages.colors["reset"]}")
        songTitle = input("Enter song title: ")
        songTitle.strip().lower()
        songTitle = titling(songTitle)
        found = False
        for song in songs:
            if songTitle == song["title"]:
                song["plays"] += 1
                messages.songRecorded()
                found = True
        if not found:
            messages.songNotFound()

# def generate_wrapped
def generate_wrapped():
    if songs:
        print(f"""{messages.colors["yellow"]}
========== YOUR SPOTIFY WRAPPED ==========

Total Songs: {totalSongs(songs)}
Total Plays: {totalPlays(songs)}
Total Listening Time: {((totalListeningTimeInSec(songs)) / 60):.2f} minutes

Your Most Played Song:
{mostPlayedSong(songs)[1]["artist"]} - {mostPlayedSong(songs)[1]["title"]} ({mostPlayedSong(songs)[0]} plays)

==========================================
        {messages.colors["reset"]}""")
    else:
        messages.songLibraryNotFound()
