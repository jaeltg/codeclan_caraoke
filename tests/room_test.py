import unittest
from classes.guest import Guest   
from classes.room import Room   
from classes.song import Song
from classes.bar import Bar

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("La Bilirrubina", "Juan Luis Guerra")
        self.song_2 = Song("Color Esperanza", "Diego Torres")
        self.song_3 = Song("Querido Tommy", "Tommy Torres")
        self.guest_1 = Guest("Andrea", 200.0, self.song_1)
        self.guest_2 = Guest("Gabriel", 100.0, self.song_3)

        songs = [self.song_1, self.song_2]
        self.room = Room("Star Room", 5, 30.0, songs)
        self.room_1 = Room("Silver Room", 2, 40.0, songs)
        
        self.drinks = [
            {"name": "Margarita",
            "price": 10.0},
            {"name": "Pisco Sour",
            "price": 11.0},
            {"name": "Chilcano",
            "price": 9.5}
        ]
        self.food = [
            {"name": "Ceviche",
            "price": 8.0},
            {"name": "Taquitos",
            "price": 10.5},
            {"name": "Chips and Guac",
            "price": 6.5}
        ]
        self.bar = Bar(self.drinks, self.food)  

    def test_room_has_name(self):
        self.assertEqual("Star Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity) 

    def test_room_has_fee(self):
        self.assertEqual(30.0, self.room.fee)

    def test_room_has_songs(self):
        self.assertEqual(2, self.room.count_songs())

    def test_can_check_amount_of_songs_in_room_playlist(self):
        self.assertEqual(2, self.room.count_songs())

    def test_can_add_song_to_playlist(self):
        song = Song("Si Vinieras por Mi", "Barbara y Fiorella Cayo")
        self.room.add_song(song)
        self.assertEqual(3, self.room.count_songs()) 

    def test_can_check_in_guest__capacity(self):
        self.room.check_in_guest(self.guest_1)
        self.assertEqual(1, self.room.count_guests())
        self.assertEqual(170.0, self.guest_1.wallet)
        self.assertEqual(30.0, self.room.total_cash)

    def test_can_check_in_guest__no_capacity(self):
        guest = Guest("Arianna", 150.0, self.song_2)
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2) 
        self.room_1.check_in_guest(guest)
        self.assertEqual(2, self.room_1.count_guests())
        self.assertEqual(160.0, self.guest_1.wallet)
        self.assertEqual(60.0, self.guest_2.wallet)
        self.assertEqual(150.0, guest.wallet)
        self.assertEqual(80.0, self.room_1.total_cash)  

    def test_can_count_guests(self):
        self.assertEqual(0, self.room.count_guests())

    def test_can_check_out_guest(self):
        self.room.check_in_guest(self.guest_1)
        self.room.check_out_guest(self.guest_1)
        self.assertEqual(0, self.room.count_guests())

    def test_can_charge_entry_fee(self):
        self.room.charge_entry_fee(self.guest_2)
        self.assertEqual(70.0, self.guest_2.wallet)
        self.assertEqual(30.0, self.room.total_cash)

    def test_guest_can_afford_entry_fee__can_afford(self):
        self.assertEqual(True, self.room.guest_can_afford(self.guest_1))

    def test_guest_can_afford_entry_fee__cant_afford(self):
        guest = Guest("Karina", 20.0, self.song_3)
        self.assertEqual(False, self.room.guest_can_afford(guest))   

    def test_can_charge_for_food(self):
        self.room.check_in_guest(self.guest_1)
        self.room.charge_for_food(self.bar, self.food[1]["name"], self.guest_1)
        self.assertEqual(159.5, self.guest_1.wallet)
        self.assertEqual(40.5, self.room.total_cash)  

    def test_can_charge_for_drink(self):
        self.room.check_in_guest(self.guest_1)
        self.room.charge_for_drink(self.bar, self.drinks[1]["name"], self.guest_1)
        self.assertEqual(159.0, self.guest_1.wallet)
        self.assertEqual(41.0, self.room.total_cash)    


        

        
              





