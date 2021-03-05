import unittest
from classes.guest import Guest   
from classes.room import Room   
from classes.song import Song  

class TestGuest(unittest.TestCase):
   
    def setUp(self):
        self.song_1 = Song("La Bilirrubina", "Juan Luis Guerra")
        self.song_2 = Song("Color Esperanza", "Diego Torres")
        self.guest_1 = Guest("Andrea", 200)
        self.guest_2 = Guest("Gabriel", 100)

        songs = [self.song_1, self.song_2]
        self.room = Room("Star Room", 5, 35.0, songs)
        
    def test_guest_has_name(self):
        self.assertEqual("Andrea", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest_2.wallet)

    def test_guest_has_songs(self):
        self.assertEqual(0, self.guest_1.count_songs())     

    def test_guest_can_choose_song(self):
        self.guest_1.choose_song(self.song_1, self.room)
        self.assertEqual(1, self.guest_1.count_songs())          

