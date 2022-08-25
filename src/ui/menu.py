import pygame

from ui.ui_entities.size_line import Sizeline
from ui.text_holder import TextHolder
from ui.ui_entities.tick_box import TickBox
from ui.ui_entities.button import Button


class Menu:

    def __init__(self, display):

        self.display = display

        self.textholder = TextHolder()

        self.industrial_tickbox = TickBox(1280, 145)
        self.organic_tickbox = TickBox(1280, 175)

        self.dungeon_sizeline = Sizeline(1080, 1320, 320)

        self.generate_dungeon_button = Button(1080, 660, 240, 50, "Generate dungeon")

    def render_background(self):

        colour = (80, 80, 80)
        x = 1050
        y = 30
        width = 300
        height = 700    

        pygame.draw.rect(self.display, (43, 20, 20), (x-15, y-15, width+30, height + 30))
        pygame.draw.rect(self.display, colour, (x, y, width, height))

    def render_dungeon_background(self):

        colour = (40, 40, 40)

        x = 7
        y = 7

        width = 1000
        height = 790

        pygame.draw.rect(self.display, colour, (x, y, width, height))

    def render_all_text(self):

        self.textholder.render_all(self.display)

    def render_tickboxes(self):

        self.industrial_tickbox.render(self.display)
        self.organic_tickbox.render(self.display)

    def render_dungeon_sizeline(self):

        self.dungeon_sizeline.render(self.display)

    def render_generate_dungeon_button(self):

        self.generate_dungeon_button.render(self.display)

    def render_all(self):

        self.render_background()
        self.render_all_text()
        self.render_tickboxes()
        self.render_dungeon_sizeline()
        self.dungeon_sizeline.size_text.blit(self.display)
        self.render_generate_dungeon_button()


