import pygame


class Text:

    def __init__(self, text, x, y, size):

        self.font = pygame.font.SysFont("Arial", size)

        self.colour = (110, 30, 30)

        self.text = self.font.render(text, True, self.colour)

        self.x = x
        self.y = y

    def blit(self, display):

        display.blit(self.text, (self.x, self.y))

    def update_text(self, text):

        text = str(text)

        self.text = self.font.render(text, True, self.colour)
