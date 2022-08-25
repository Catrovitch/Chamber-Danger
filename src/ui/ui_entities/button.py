import pygame

from ui.ui_entities.text import Text

class Button:

    def __init__(self, x, y, width, height, text):

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.text = Text(text, x+5, y+9, 28)

        self.clicked = False

        self.colour_not_clicked = (56, 56, 56)
        self.colour_clicked = (110, 110, 110)


    def render(self, display):

        self.draw_border(display)

        if self.clicked == False:
            pygame.draw.rect(display, self.colour_not_clicked, (self.x, self.y, self.width, self.height))
        if self.clicked == True:
            pygame.draw.rect(display, self.colour_clicked, (self.x, self.y, self.width, self.height))

        self.text.blit(display)
    
    def draw_border(self, display):

        border_x = self.x -5
        border_y = self.y -5
        border_width = self.width +10
        border_height = self.height +10
        
        border_colour = (64, 17, 17)

        pygame.draw.rect(display, border_colour, (border_x, border_y, border_width, border_height))

    def is_clicked(self, pos):

        x = pos[0]
        y = pos[1]

        if self.x <= x <= (self.x+self.width):
            if self.y <= y <= (self.y+self.height):
                return True

    def update_text(self, text):

        self.text = Text(str(text), self.x+5, self.y+9, 28)