class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
        self.songs = []
        
    def count_songs(self):
        return len(self.songs)    

    def choose_song(self, song, room):
        if song in room.songs:
            self.songs.append(song)    

    def request_song(self, song, room):
        if song not in room.songs:
            room.add_song(song)
            self.choose_song(song, room)
        elif song in room.songs:
            self.choose_song(song, room)    

               