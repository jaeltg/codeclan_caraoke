class Room:
    def __init__(self, name, capacity, fee, songs):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.songs = songs
        self.guests = []

    def count_songs(self):
        return len(self.songs)    

    def add_song(self, song):
        self.songs.append(song)

    def count_guests(self):
        return len(self.guests)

    def check_in_guest(self, guest):
         self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)     

