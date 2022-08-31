import unittest
from services.OrganicBSPDungeon import OrganicBSPDungeon


class TestBSPDungeon(unittest.TestCase):

    def setUp(self):

        self.dungeon = OrganicBSPDungeon()

    def test_constructor_map_len(self):

        self.assertEqual(len(self.dungeon.map), 0)

    def test_constructor_chamber(self):

        self.assertEqual(self.dungeon.chamber, None)

    def test_generateMap_map_width(self):

        self.dungeon.generateMap()

        self.assertEqual(self.dungeon.map_width, 100)

    def test_generateMap_map_height(self):

        self.dungeon.generateMap()

        self.assertEqual(self.dungeon.map_height, 80)

    def test_initiate_map(self):

        self.dungeon.generateMap()

        self.dungeon._initiate_map()

        test = True

        for row in range(100):
            for item in range(80):
                print(row, item)
                if self.dungeon.map[row][item] != 1:
                    test = False

        self.assertEqual(test, True)

    def test_node_size_is_max(self):

        self.dungeon.max_node_size = 150

        self.dungeon.generateMap()

        number_of_nodes = len(self.dungeon._nodes)

        self.assertEqual(number_of_nodes, 1)
