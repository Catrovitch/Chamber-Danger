import unittest
from services.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):

        self.room = Room(10, 15, 20, 25)

    def test_constructor_x(self):

        self.assertEqual(self.room.x, 10)

    def test_constructor_y(self):

        self.assertEqual(self.room.y, 15)

    def test_constructor_width(self):

        self.assertEqual(self.room.width, 20)

    def test_constructor_height(self):

        self.assertEqual(self.room.height, 25)

    def test_constructor_colour(self):

        self.assertEqual(self.room.colour, (92, 92, 92))