
import unittest
from services.node import Node
from services.BSPDungeon import BSPDungeon


class TestNode(unittest.TestCase):

    def setUp(self):

        self.node = Node(10, 15, 20, 25)

    def test_constructor_x(self):

        self.assertEqual(self.node.x, 10)

    def test_constructor_y(self):

        self.assertEqual(self.node.y, 15)

    def test_constructor_width(self):

        self.assertEqual(self.node.width, 20)

    def test_constructor_height(self):

        self.assertEqual(self.node.height, 25)

    def test_constructor_min_node_size(self):

        self.assertEqual(self.node.min_node_size, 10)

    def test_constructor_child_1(self):

        self.assertEqual(self.node.child_1, None)

    def test_constructor_child_2(self):

        self.assertEqual(self.node.child_2, None)

    def test_constructor_chamber(self):

        self.assertEqual(self.node.chamber, None)

    def test_constructor_tunnel(self):

        self.assertEqual(self.node.tunnel, None)

    def test_splitNode_no_children(self):

        self.assertEqual(self.node.splitNode(), True)

    def test_splitNode_too_small_to_split(self):

        self.node = Node(10, 15, 12, 15)

        self.assertEqual(self.node.splitNode(), False)

    def test_splitNode_split_successful(self):

        self.assertEqual(self.node.splitNode(), True)

    def test_createChambers(self):

        dungeon = BSPDungeon()
        dungeon.generateMap(80, 50)
