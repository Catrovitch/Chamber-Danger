class Chamber: # used for the tunneling algorithm
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x+w
        self.y2 = y+h

    def center(self):
        centerX = int((self.x1 + self.x2)/2)
        centerY = int((self.y1 + self.y2)/2)
        return (centerX, centerY)

    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
        self.y1 <= other.y2 and self.y2 >= other.y1)