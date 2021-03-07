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

# Can I do drink and food functions in just one?
    def find_food_by_name(self, bar, food_name):
        result_food = None

        for food in bar.food:
             if food["name"] == food_name:
                result_food = food   
                
        return result_food

    def charge_for_food(self, bar, food_name, guest):
        food = self.find_food_by_name(bar, food_name)
        if guest in self.guests:
            guest.pay(food["price"])
            self.total_cash += food["price"]

    def find_drink_by_name(self, bar, drink_name):
        result_drink = None

        for drink in bar.drinks:
             if drink["name"] == drink_name:
                result_drink = drink
                
        return result_drink

    def charge_for_drink(self, bar, drink_name, guest):
        drink = self.find_drink_by_name(bar, drink_name)
        if guest in self.guests:
            guest.pay(drink["price"])
            self.total_cash += drink["price"]        



