import pygame

from ui.ui_entities.text import Text


class TickBox:

    def __init__(self, x, y, title):

        """A class that functions as a tickbox for the GUI.
        """

        self.colour = (220, 149, 149)

        self.ticked = False
        self.width = 13
        self.height = 13

        self.x = x
        self.y = y

        self.title = Text(title, self.x-200, self.y-3, 20)

    def is_clicked(self, pos):

        x = pos[0]
        y = pos[1]

        if self.x <= x <= (self.x+self.width):
            if self.y <= y <= (self.y+self.height):
                return True

    def render(self, display):

        self.render_border(display)

        self.render_tickbox(display)

        self.title.blit(display)

        if self.ticked:

            self.render_x(display)

    def render_border(self, display):

        border_colour = (56, 56, 56)
        border_x = self.x-4
        border_y = self.y-4
        border_width = 20
        border_height = 20

        pygame.draw.rect(display, (border_colour), (border_x,
                         border_y, border_width, border_height))

    def render_tickbox(self, display):

        pygame.draw.rect(display, (self.colour),
                         (self.x, self.y, self.width, self.height))

    def render_x(self, display):

        x_colour = (10, 10, 10)

        line1_start = (self.x, self.y)
        line1_end = (self.x+self.width, self.y+self.height)

        line2_start = (self.x, self.y+self.height)
        line2_end = (self.x+self.width, self.y)

        pygame.draw.line(display, (x_colour), (line1_start), (line1_end), 3)
        pygame.draw.line(display, (x_colour), (line2_start), (line2_end), 3)
