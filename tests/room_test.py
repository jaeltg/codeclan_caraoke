import unittest
from classes.guest import Guest   
from classes.room import Room   
from classes.song import Song  

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("La Bilirrubina", "Juan Luis Guerra")
        self.song_2 = Song("Color Esperanza", "Diego Torres")
        self.guest_1 = Guest("Andrea", 200)
        self.guest_2 = Guest("Gabriel", 100)

        songs = [self.song_1, self.song_2]
        self.room = Room("Star Room", 5, 35.0, songs)

    def test_room_has_name(self):
        self.assertEqual("Star Room", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.capacity) 

    def test_room_has_fee(self):
        self.assertEqual(35.0, self.room.fee)

    def test_room_has_songs(self):
        self.assertEqual(2, self.room.count_songs())

    def test_can_check_amount_of_songs_in_room_catalogue(self):
        self.assertEqual(2, self.room.count_songs())

    def test_can_add_song_to_catalogue(self):
        song = Song("Si Vinieras por Mi", "Barbara y Fiorella Cayo")
        self.add_song(song)
        self.assertEqual(3, self.room.count_songs())            



