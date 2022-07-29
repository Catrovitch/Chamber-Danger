import unittest
from services.dungeon import Dungeon

class TestDungeon(unittest.TestCase):

    def setUp(self):

        self.dungeon = Dungeon()

    def test_constructor_map_type(self):

        map_type = type(self.dungeon.map)

        self.assertEqual(map_type, dict)

    def test_constructor_map_length(self):

        map_length = len(self.dungeon.map)

        self.assertEqual(map_length, 0)

    def test_constructor_rooms_type(self):

        rooms_type = type(self.dungeon.rooms)

        self.assertEqual(rooms_type, list)

    def test_constructor_rooms_length(self):

        rooms_length = len(self.dungeon.rooms)

        self.assertEqual(rooms_length, 0)

    def test_create_map(self):

        self.dungeon.create_map()

        all_values_zero = True

        for key, value in self.dungeon.map.items():
            if value != 0:
                all_values_zero = False
        
        self.assertEqual(all_values_zero, True)