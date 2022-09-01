import random
from entities.node import Node
from entities.corridor import Corridor


class OrganicBSPDungeon:

    """A BSP algorithm connected by Drankard's walk algorithm"""

    def __init__(self, max_node_size=24, max_chamber_size=15, min_chamber_size=5):

        self.map = []
        self.chamber = None
        self.max_node_size = 24
        self.max_chamber_size = 15
        self.min_chamber_size = 6
        self.organic = True
        self.organic_level = 1.
        self.fitting = 3

        self.chambers = []
        self.drunkardswalk = []
        self.graph_visualizer = []

        self.min_chamber_level = 0
        self.max_chamber_level = 10000000

    def generateMap(self):
       
        """Initializes/resets 2D list
        """

        self.map_width = 100
        self.map_height = 80

        self._initiate_map()

        self._nodes = []

        root_node = Node(0, 0, self.map_width, self.map_height, 0)
        self._nodes.append(root_node)

        splitted = True
        # loop and split nodes until not possible
        while (splitted):
            splitted = False
            for node in self._nodes:
                if (node.child_1 == None) and (node.child_2 == None):
                    if ((node.width > self.max_node_size) or
                            (node.height > self.max_node_size)):
                        if (node.splitNode()):
                            self._nodes.append(node.child_1)
                            self._nodes.append(node.child_2)
                            splitted = True

        root_node.createChambers(self)

        self.chamber_depth()

        return self.map

    def _initiate_map(self):

        """Creates a 2d matrix according to the map_height and map_width.
        """

        self.map = [[1
                     for y in range(self.map_height)]
                    for x in range(self.map_width)]

        self.drunkardswalk = [[1
                               for y in range(self.map_height)]
                              for x in range(self.map_width)]

    def createChamber(self, chamber):
        """sets the values in the map list which corresponds to the given chamber from 1 to 0
        """

        for x in range(chamber.x1 + 1, chamber.x2):
            for y in range(chamber.y1+1, chamber.y2):
                self.map[x][y] = 0

        if len(self.chambers) == 0:
            self.min_chamber_level = chamber.number
            self.max_chamber_level = chamber.number
        
        if chamber.number < self.min_chamber_level:
            self.min_chamber_level = chamber.number

        if chamber.number > self.max_chamber_level:
            self.max_chamber_level = chamber.number

        self.dungeon_depth = self.max_chamber_level - self.min_chamber_level

        self.chambers.append(chamber)

    def createTunnel(self, chamber1, chamber2):
        """heavily weighted drunkards walk algorithm
        """
        drunk_x, drunk_y = chamber2.center()
        goal_x, goal_y = chamber1.center()

        x1, y1 = chamber1.center()
        x2, y2 = chamber2.center()

        while not (chamber1.x1 <= drunk_x <= chamber1.x2) or not (chamber1.y1 < drunk_y < chamber1.y2):
            # Choose the direction of the drunk
            up = 1.0
            down = 1.0
            right = 1.0
            left = 1.0

            weight = 1

            # weight against edges
            if drunk_x < goal_x:  # drunk is left of goal
                right += weight
            elif drunk_x > goal_x:  # drunk is right of goal
                left += weight
            if drunk_y < goal_y:  # drunk is above goal
                down += weight
            elif drunk_y > goal_y:  # drunk is below goal
                up += weight

            # probabilities are normalized
            total = up+down+right+left
            up /= total
            down /= total
            right /= total
            left /= total

            # choose the direction
            direction = random.random()
            if 0 <= direction < up:
                h_x = 0
                h_y = -1
            elif up <= direction < (up+down):
                h_x = 0
                h_y = 1
            elif (up+down) <= direction < (up+down+right):
                h_x = 1
                h_y = 0
            else:
                h_x = -1
                h_y = 0

            # collision at edges are checked here
            if (0 < drunk_x+h_x < self.map_width-1) and (0 < drunk_y+h_y < self.map_height-1):
                drunk_x += h_x
                drunk_y += h_y
                if self.map[drunk_x][drunk_y] == 1:
                    self.map[drunk_x][drunk_y] = 0
                    self.drunkardswalk[drunk_x][drunk_y] = chamber1.colour

        self.graph_visualizer.append(
            Corridor(chamber1, chamber2, chamber1.colour, x1, y1, x2, y2))

    def chamber_depth(self):

        for chamber in self.chambers:
            chamber.depth(self.dungeon_depth, self.min_chamber_level)