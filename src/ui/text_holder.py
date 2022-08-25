import pygame

from ui.ui_entities.text import Text


class TextHolder:

    def __init__(self):

        self.title = Text("Chamber-Danger", 1080, 45, 34)
        
        self.choose_dungeon_type_text = Text("Choose dungeon type:", 1080, 110, 23)
        self.industrial_text = Text("Industrial dungeon:", 1100, 140, 20)
        self.organic_text = Text("Organic dungeon:", 1100, 170, 20)

        self.choose_dungeon_size_text = Text("Choose dungeon size:", 1080, 250, 23)


    def render_all(self, display):

        self.title.blit(display)

        self.choose_dungeon_type_text.blit(display)

        self.choose_dungeon_size_text.blit(display)

        self.industrial_text.blit(display)

        self.organic_text.blit(display)


