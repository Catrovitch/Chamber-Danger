
import unittest
from services.BSPDungeon import BSPDungeon


class TestBSPDungeon(unittest.TestCase):

    def setUp(self):

        self.dungeon = BSPDungeon()

    def test_constructor_map_len(self):

        self.assertEqual(len(self.dungeon.map), 0)

    def test_constructor_chamber(self):

        self.assertEqual(self.dungeon.chamber, None)

    def test_generate_map(self):

        pass
