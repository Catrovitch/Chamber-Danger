class Room:
    """Defines a room of the dungeon."""
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = (92, 92, 92)
                
    def __str__(self):
        return f"A room at ({self.x},{self.y})"