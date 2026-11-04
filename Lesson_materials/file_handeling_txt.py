songlist = []


#load songs into songlist:
with open("songlist.txt", "r") as song_library:
    for line in song_library:
        songlist.append(line.strip())

print("Songs loaded:", songlist)

#add song to playlist
song_name = input("Enter the name of the song to add:\n ")
songlist.append(song_name)

with open("songlist.txt", "w") as song_library:
     for i in songlist:
         song_library.write(i +"\n")

