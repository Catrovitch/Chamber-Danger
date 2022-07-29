class Room:
    """Defines a room of the dungeon."""
    def __init__(self,x,y,width,height):
        self.x1 = x
        self.y1 = y

        self.width = width
        self.height = height
        
        self.x2 = self.x1 + self.width
        self.y2 = self.y1 + self.height
