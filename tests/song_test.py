import unittest
from classes.song import Song  

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song = Song("La Bilirrubina", "Juan Luis Guerra")
    
    def test_song_has_name(self):
        self.assertEqual("La Bilirrubina", self.song.name)

    def test_song_has_singer(self):
        self.assertEqual("Juan Luis Guerra", self.song.singer)
        

