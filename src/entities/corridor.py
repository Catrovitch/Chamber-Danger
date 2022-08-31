class Corridor:

    """This class holds information about the graph that is created by the BSP algorithm. 
        It is used by the GUI to visualize the paths of the graph.
    """

    def __init__(self, parent, child, colour, x1, y1, x2, y2):

        self.parent = parent
        self.child = child
        self.colour = colour
        
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


        