class Room:
    def __init__(self, name, capacity, fee, songs):
        self.name = name
        self.capacity = capacity
        self.fee = fee
        self.songs = songs
        self.total_cash = 0
        self.guests = []
        
    def count_songs(self):
        return len(self.songs)    

    def add_song(self, song):
        self.songs.append(song)

    def count_guests(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        if len(self.guests) < self.capacity and self.guest_can_afford(guest):
            self.guests.append(guest)
            self.charge_entry_fee(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def guest_can_afford(self, guest):
        return guest.wallet > self.fee 

    def charge_entry_fee(self, guest):
        if self.guest_can_afford(guest):
            guest.pay(self.fee)
            self.total_cash += self.fee          


