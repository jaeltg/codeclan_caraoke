import unittest
from classes.guest import Guest   
from classes.room import Room   
from classes.song import Song  

class TestGuest(unittest.TestCase):
   
    def setUp(self):
        self.song = Song("La Bilirrubina", "Juan Luis Guerra")
        self.guest_1 = Guest("Andrea", 200)
        self.guest_2 = Guest("Gabriel", 100)
        
    def test_guest_has_name(self):
        self.assertEqual("Andrea", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(100, self.guest_2.wallet)        

