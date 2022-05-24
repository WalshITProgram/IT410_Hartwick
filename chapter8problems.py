# problem 8-1
def displayRadioStation(radioStation):
    print("Let me tune in " + radioStation)

favRadioStation = input("Please enter your favorite radio station ")
float(favRadioStation)
displayRadioStation(favRadioStation)

# problem 8-2
def print_business_cards(name, quantity, tag_line_info):
    print(f"Currenly printing {quantity} businesss cards for {name}. The tag line will be '{tag_line_info}'")

print_business_cards("Best Buy", 200, "Making technology work for you!")
print_business_cards("Target", 150, "Expect more, pay less!")
print_business_cards("MJR", 250, "Its more fun at MJR!")

# problem 8-3
def print_business_cards_modifed(name, tag_line_info,quantity=100):
    print(f"Currenly printing {quantity} businesss cards for {name}. The tag line will be '{tag_line_info}'")

print_business_cards_modifed("Best Buy", "Making technology work for you!", 150)
print_business_cards_modifed("Target", "Expect more, pay less!")

# problem 8-4
def songInfomation(title, artist="Unknown"):
    formattedString = f"{title} by {artist}"
    return formattedString

formattedSong = songInfomation("Starboy", "The Weeknd")
print(formattedSong)
formattedSong = songInfomation("Closer", "The Chainsmokers")
print(formattedSong)
formattedSong = songInfomation("Takeaway")
print(formattedSong)

# problem 8-5
def songDictionary(title, artist="Unknown"):
    dictionaryItem = {'title': title, 'artist': artist}
    return dictionaryItem
def printSongEntries(songInfo):
    print("Here are all the song entries in the list:")
    for song in songInfo:
        print(song)

playlist = []

while True:
    song = input("Enter a song or q to quit: ")
    if song == "q":
        break
    artist = input("Enter a artist for that song or q to quit: ")
    dictionarySong = songDictionary(song, artist)
    playlist.append(dictionarySong)
printSongEntries(playlist)

