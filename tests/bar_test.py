import unittest
from classes.bar import Bar

class TestBar(unittest.TestCase):
    
    def setUp(self):
        self.drinks = [
            {"name": "Margarita",
            "price": 10.0},
            {"name": "Pisco Sour",
            "price": 11.0},
            {"name": "Chilcano",
            "price": 9.5}
        ],
        self.food = [
            {"name": "Ceviche",
            "price": 8.0},
            {"name": "Taquitos",
            "price": 10.5},
            {"name": "Chips and Guac",
            "price": 6.5}
        ]
        self.bar = Bar(self.drinks, self.food)  
    
    def test_bar_has_drinks(self):
        self.assertEqual(self.drinks, self.bar.drinks)
        
    def test_bar_has_food(self):
        self.assertEqual(self.food, self.bar.food)
      
        