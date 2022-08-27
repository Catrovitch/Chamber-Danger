import pygame

from ui.ui_entities.text import Text


class TextHolder:

    def __init__(self):

        self.title = Text("Chamber-Danger", 1080, 45, 34)
        
        self.choose_dungeon_type_text = Text("Choose dungeon type:", 1080, 110, 23)


    def render_all(self, display):

        self.title.blit(display)

        self.choose_dungeon_type_text.blit(display)

