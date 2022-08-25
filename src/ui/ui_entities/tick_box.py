import pygame

class TickBox:

    def __init__(self, x, y):

        self.colour = (220, 149, 149)

        self.ticked = False
        self.width = 10
        self.height = 10

        self.x = x
        self.y = y

    def is_clicked(self, pos):

        x = pos[0]
        y = pos[1]

        if self.x <= x <= (self.x+self.width):
            if self.y <= y <=(self.y+self.height):
                return  True

    def render(self, display):

        self.render_border(display)
        
        self.render_tickbox(display)    

        if self.ticked:
            
            self.render_x(display)


    def render_border(self, display):

        border_colour = (56, 56, 56)
        border_x = self.x-3
        border_y = self.y-3
        border_width = 16
        border_height = 16

        pygame.draw.rect(display, (border_colour), (border_x, border_y, border_width, border_height))


    def render_tickbox(self, display):

        pygame.draw.rect(display, (self.colour), (self.x, self.y, self.width, self.height))


    def render_x(self, display):

        x_colour = (10, 10 ,10)
        
        line1_start = (self.x, self.y)
        line1_end = (self.x+self.width, self.y+self.height)

        line2_start = (self.x, self.y+self.height)
        line2_end = (self.x+self.width, self.y)

        pygame.draw.line(display, (x_colour), (line1_start), (line1_end), 2)
        pygame.draw.line(display, (x_colour), (line2_start), (line2_end), 2)



