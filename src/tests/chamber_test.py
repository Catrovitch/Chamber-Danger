
import unittest
from entities.chamber import Chamber


class TestChamber(unittest.TestCase):

    def setUp(self):

        self.chamber = Chamber(10, 15, 20, 25, 0)

    def test_constructor_x1(self):

        self.assertEqual(self.chamber.x1, 10)

    def test_constructor_y1(self):

        self.assertEqual(self.chamber.y1, 15)

    def test_constructor_x2(self):

        self.assertEqual(self.chamber.x2, 30)

    def test_constructor_y2(self):

        self.assertEqual(self.chamber.y2, 40)

    def test_center(self):

        center_x, center_y = self.chamber.center()

        self.assertEqual((center_x, center_y), (20, 27))
