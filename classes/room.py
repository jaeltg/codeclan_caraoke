class Room:
    def __init__(self, name, capacity, fee, songs):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.songs = songs

    def count_songs(self):
        return len(self.songs)    

    # def add_song(self):    