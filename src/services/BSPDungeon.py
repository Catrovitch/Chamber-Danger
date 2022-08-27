import random
from entities.node import Node

# ==== A BSP based dungeon ====


class BSPDungeon:
    def __init__(self, max_node_size=24, max_chamber_size=15, min_chamber_size=5):
        self.map = []
        self.chamber = None
        self.max_node_size = max_node_size
        self.max_chamber_size = max_chamber_size
        self.min_chamber_size = min_chamber_size

    
    def generateMap(self):
        # Initializes/resets 2D list

        self.map_width = 100
        self.map_height = 80

        self._initiate_map()

        self._nodes = []

        root_node = Node(0, 0, self.map_width, self.map_height)
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

        return self.map

    
    def _initiate_map(self):

        self.map = [[1
                     for y in range(self.map_height)]
                    for x in range(self.map_width)]


    
    def createChamber(self, chamber):
        # sets the values in the map lists which corresponds to the given chamber from 1 to 0
        for x in range(chamber.x1 + 1, chamber.x2):
            for y in range(chamber.y1+1, chamber.y2):
                self.map[x][y] = 0

    
    def createTunnel(self, chamber1, chamber2):
        # digs a tunnel from chamber1 to chamber2
        x1, y1 = chamber1.center()
        x2, y2 = chamber2.center()
        # 50/50 if tunnel is horizontal or vertical
        if random.randint(0, 1) == 1:
            self.createHorizontalTunnel(x1, x2, y1)
            self.createVerticalTunnel(y1, y2, x2)

        else:
            self.createVerticalTunnel(y1, y2, x1)
            self.createHorizontalTunnel(x1, x2, y2)

    
    def createHorizontalTunnel(self, x1, x2, y):

        for x in range(min(x1, x2), max(x1, x2)+1):
            self.map[x][y] = 0

    
    def createVerticalTunnel(self, y1, y2, x):

        for y in range(min(y1, y2), max(y1, y2)+1):
            self.map[x][y] = 0