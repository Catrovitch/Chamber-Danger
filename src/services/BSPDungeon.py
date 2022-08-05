import random
from services.node import Node

# ==== A BSP based dungeon ====
class BSPDungeon:
    def __init__(self):
        self.map = []
        self.chamber = None
        self.max_node_size = 24
        self.max_chamber_size = 15
        self.min_chamber_size = 6
 
    def generateMap(self, map_width, map_height):
        # Initializes/resets 2D list

        self.map_width = map_width
        self.map_height = map_height

        self.map = [[1
            for y in range(map_height)]
                for x in range(map_width)]

        self._nodes = []

        root_node = Node(0,0,map_width,map_height)
        self._nodes.append(root_node)

        splitted = True
        # loop and split nodes until not possible
        while (splitted):
            splitted = False
            for node in self._nodes:
                if (node.child_1 == None) and (node.child_2 == None):
                    if ((node.width > self.max_node_size) or 
                    (node.height > self.max_node_size) or
                    (random.random() > 0.8)):
                        if (node.splitNode()):
                            self._nodes.append(node.child_1)
                            self._nodes.append(node.child_2)
                            splitted = True

        root_node.createChambers(self)

        return self.map

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
        if random.randint(0,1) == 1:
            self.createHorizontalTunnel(x1, x2, y1)
            self.createVerticalTunnel(y1, y2, x2)

        else:
            self.createVerticalTunnel(y1, y2, x1)
            self.createHorizontalTunnel(x1, x2, y2)

    def createHorizontalTunnel(self, x1, x2, y):
        
        for x in range(min(x1,x2),max(x1,x2)+1):
            self.map[x][y] = 0

    def createVerticalTunnel(self, y1, y2, x):
        
        for y in range(min(y1,y2),max(y1,y2)+1):
            self.map[x][y] = 0

    def get_nodes(self):
        #prints out all node objects.
        for node in self._nodes:
            print(node)