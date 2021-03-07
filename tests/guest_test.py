import unittest
from classes.guest import Guest   
from classes.room import Room   
from classes.song import Song
from classes.bar import Bar

class TestGuest(unittest.TestCase):
   
    def setUp(self):
        self.song_1 = Song("La Bilirrubina", "Juan Luis Guerra")
        self.song_2 = Song("Color Esperanza", "Diego Torres")
        self.song_3 = Song("Querido Tommy", "Tommy Torres")
        self.guest_1 = Guest("Andrea", 200.0, self.song_1)
        self.guest_2 = Guest("Gabriel", 100.0, self.song_3)

        songs = [self.song_1, self.song_2]
        self.room = Room("Star Room", 5, 35.0, songs)

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
        
    def test_guest_has_name(self):
        self.assertEqual("Andrea", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest_2.wallet)

    def test_guest_has_songs(self):
        self.assertEqual(0, self.guest_1.count_songs())

    def test_guest_has_favourite_song(self):
         self.assertEqual("Querido Tommy", self.guest_2.favourite_song.name)        

    def test_guest_can_request_song__song_not_in_playlist(self):
        song = Song("Si Vinieras por Mi", "Barbara y Fiorella Cayo")
        self.guest_1.request_song(song, self.room)
        self.assertEqual(3, self.room.count_songs())
        self.assertEqual(1, self.guest_1.count_songs()) 

    def test_guest_can_request_song__song_in_playlist(self):
        self.guest_1.request_song(self.song_1, self.room)
        self.assertEqual(2, self.room.count_songs())
        self.assertEqual(1, self.guest_1.count_songs())

    def test_guest_can_pay(self):
         self.guest_1.pay(30.0)
         self.assertEqual(170.0, self.guest_1.wallet)

    def test_favourite_song_in_room_playlist(self):
        self.assertEqual("Wooohooo, yeesss!!!", self.guest_1.favourite_song_in_room_playlist(self.room))

    def test_can_choose_food_by_name(self):
        food = self.guest_1.choose_food_by_name(self.bar, self.food[1]["name"])
        self.assertEqual("Taquitos", food["name"])

    def test_can_choose_drink_by_name(self):
        drink = self.guest_1.choose_drink_by_name(self.bar, self.drinks[1]["name"])
        self.assertEqual("Pisco Sour", drink["name"])      



