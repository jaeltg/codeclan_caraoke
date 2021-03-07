class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.songs = []
        self.favourite_song = favourite_song
        
    def count_songs(self):
        return len(self.songs)             

    # Can I use list comprehension for this?
    def request_song(self, song, room):
        if song not in room.songs:
            room.add_song(song)
            self.songs.append(song)
        elif song in room.songs:
            self.songs.append(song)     

    def pay(self, amount):
        self.wallet -= amount  

    def favourite_song_in_room_playlist(self, room):
        if self.favourite_song in room.songs:
            return "Wooohooo, yeesss!!!"


               