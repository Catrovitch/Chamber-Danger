import random
from services.chamber import Chamber
class Node:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_node_size = 10
        self.child_1 = None
        self.child_2 = None
        self.chamber = None
        self.tunnel = None

    def splitNode(self):
        
        if (self.child_1 != None) or (self.child_2 != None):
            return False # This leaf has already been split

        '''
        ==== Determine the direction of the split ====
        If the width of the leaf is >25% larger than the height,
        split the leaf vertically.
        If the height of the leaf is >25 larger than the width,
        split the leaf horizontally.
        Otherwise, choose the direction at random.
        '''
        horizontal_split = random.choice([True, False])

        if (self.width/self.height >= 1.25):
            horizontal_split = False
        elif (self.height/self.width >= 1.25):
            horizontal_split = True

        if (horizontal_split):
            max = self.height - self.min_node_size
        else:
            max = self.width - self.min_node_size

        if (max <= self.min_node_size):
            return False # the leaf is too small to split further

        split = random.randint(self.min_node_size,max) #determine where to split the leaf

        if (horizontal_split):
            self.child_1 = Node(self.x, self.y, self.width, split)
            self.child_2 = Node( self.x, self.y+split, self.width, self.height-split)
        else:
            self.child_1 = Node( self.x, self.y,split, self.height)
            self.child_2 = Node( self.x + split, self.y, self.width-split, self.height)

        return True

    def createChambers(self, dungeon):
        
        if (self.child_1) or (self.child_2):
        # recursively search for children until you hit the end of the branch
            if (self.child_1):
                self.child_1.createChambers(dungeon)
            if (self.child_2):
                self.child_2.createChambers(dungeon)

            if (self.child_1 and self.child_2):
                dungeon.createTunnel(self.child_1.getChamber(),
                    self.child_2.getChamber())

        else:
        # Create rooms in the end branches of the bsp tree
            width = random.randint(dungeon.min_chamber_size, min(dungeon.max_chamber_size,self.width-1))
            height = random.randint(dungeon.min_chamber_size, min(dungeon.max_chamber_size,self.height-1))
            x = random.randint(self.x, self.x+(self.width-1)-width)
            y = random.randint(self.y, self.y+(self.height-1)-height)
            self.chamber = Chamber(x,y,width,height)
            dungeon.createChamber(self.chamber)

    def getChamber(self):
        if (self.chamber): return self.chamber

        else:
            if (self.child_1):
                self.room_1 = self.child_1.getChamber()
            if (self.child_2):
                self.room_2 = self.child_2.getChamber()

            if (not self.child_1 and not self.child_2):
                # neither room_1 nor room_2
                return None

            elif (not self.room_2):
                # room_1 and !room_2
                return self.room_1

            elif (not self.room_1):
                # room_2 and !room_1
                return self.room_2

            # If both room_1 and room_2 exist, pick one
            elif (random.random() < 0.5):
                return self.room_1
            else:
                return self.room_2