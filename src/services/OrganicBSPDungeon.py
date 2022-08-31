import random
from entities.node import Node


# === A BSP based dungeon connected by Drunkard's walk algorithm ===
class OrganicBSPDungeon:

    def __init__(self, max_node_size=24, max_chamber_size=15, min_chamber_size=5):

        self.map = []
        self.chamber = None
        self.max_node_size = 24
        self.max_chamber_size = 15
        self.min_chamber_size = 6
        self.organic = True
        self.organic_level = 1.
        self.fitting = 3

    
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
        self.clean_map(self.map_width, self.map_height)

        return self.map

    
    def _initiate_map(self):

        self.map = [[1
                     for y in range(self.map_height)]
                    for x in range(self.map_width)]


    
    def createChamber(self, room):
        # sets the values in the map list which corresponds to the given chamber from 1 to 0
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1+1, room.y2):
                self.map[x][y] = 0

    
    def createTunnel(self, chamber1, chamber2):
        # heavily weighted drunkards walk algorithm

        drunk_x, drunk_y = chamber2.center()
        goal_x, goal_y = chamber1.center()

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

    
    def clean_map(self, mapWidth, mapHeight):
        if (self.organic):
            for i in range(3):
                # Look at each value in map and see if it's smooth
                for x in range(1, mapWidth-1):
                    for y in range(1, mapHeight-1):
                        if (self.map[x][y] == 1) and (self.getAdjacentWall(x, y) <= self.organic_level):
                            self.map[x][y] = 0

                        if (self.map[x][y] == 0) and (self.getAdjacentWall(x, y) >= self.fitting):
                            self.map[x][y] = 1

    
    def getAdjacentWall(self, x, y):
        # locates walls in all directions
        wall_count = 0

        if (self.map[x][y-1] == 1):  # Check up
            wall_count += 1
        if (self.map[x][y+1] == 1):  # Check down
            wall_count += 1
        if (self.map[x-1][y] == 1):  # Check left
            wall_count += 1
        if (self.map[x+1][y] == 1):  # Check right
            wall_count += 1

        return wall_count
