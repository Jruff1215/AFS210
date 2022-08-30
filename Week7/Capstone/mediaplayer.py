import doublyLinked

#print(doublyLinked)
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title) == (other))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
songList = doublyLinked.DoublyLinkedList()
song = doublyLinked.Node(Song('No Role Modelz', 'J.Cole'))
songList.addLast(song)
song = doublyLinked.Node(Song('Loyalty', 'Kendrick Lamar'))
songList.addLast(song)
song = doublyLinked.Node(Song('Weak', 'SWV'))
songList.addLast(song)
song = doublyLinked.Node(Song('Sleep At Night', 'Chris Brown'))
songList.addLast(song)
song = doublyLinked.Node(Song('Get Back', 'Mario'))
songList.addLast(song)
song = doublyLinked.Node(Song('Love', 'Musiq SoulChild'))
songList.addLast(song)
song = doublyLinked.Node(Song('Baccseat', 'Roddy Rich'))
songList.addLast(song)


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    #print(songList)
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        def addSong():
            songTitle = input('Enter the song title: ')
            songArtist = input('Enter the song artist: ')
            song = doublyLinked.Node(Song(songTitle, songArtist))
            songList.addLast(song)
        addSong()
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        deleteSong = input('Enter the song title: ')
        #print(deleteSong)
        songList.delete(deleteSong)
        # remove song from playlist
        print("Song Removed to Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        if songList.current is None:
            songList.current = songList.head
            
        print("Playing....", songList.current.data.data)        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        if songList.current is None:
            songList.current = songList.head
        else:
            if songList.current.next is not None:
                songList.current = songList.current.next           
            else:
                songList.current = songList.head
        print("Skipping....", songList.current.data.data)                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        def prevSong():
            if songList.current is None:
                songList.current = songList.tail
            else:
                if songList.current.prev is not None:
                    songList.current = songList.current.prev           
                else:
                    songList.current = songList.tail
        prevSong()
        print("Replaying....", songList.current.data.data)  
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("_____________________________________________")
        songList.shuffle()
        print("_____________________________________________")

       # print(songList)
        print("Shuffling....")          
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", songList.current.data.data)    
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        print(songList)
    elif choice == 0:
        print("Goodbye.")
        break

            
