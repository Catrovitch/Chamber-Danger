from random import randrange

class Chamber:
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
        center_x = (self.x1 + self.x2)//2
        center_y = (self.y1 + self.y2)//2
        return (center_x, center_y)

