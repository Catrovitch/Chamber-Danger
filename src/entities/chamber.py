from random import randrange

class Chamber:

    """This class functions as a visual presentation of the nodes of the graph created by the BSP algorithm.
    """
    def __init__(self, x, y, w, h, number):
        self.x1 = x
        self.y1 = y
        self.height = h
        self.width = w
        self.x2 = x+w
        self.y2 = y+h
        self.number = number

        self.colour = (randrange(0, 255), randrange(0, 255), randrange(0, 255))

    def center(self):

        """Finds and returns the center of the chamber.

        Returns:
            tuple: x, y (center of the circle)
        """
        center_x = (self.x1 + self.x2)//2
        center_y = (self.y1 + self.y2)//2
        return (center_x, center_y)

    def depth(self, interval, min_level):

        dungeon_colour_level = self.number-min_level

        depth_interval = 255//interval

        depth_level = 255-dungeon_colour_level*depth_interval
        self.depth_colour = (depth_level, depth_level, depth_level)

