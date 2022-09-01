import pygame

from ui.ui_entities.text import Text


class TextHolder:

    def __init__(self):
        """This class is a utility class to keep track of text elements in the UI.
        """

        self.title = Text("Chamber-Danger", 1080, 45, 34)

        self.choose_dungeon_type_text = Text(
            "Choose dungeon type:", 1080, 110, 23)

    def render_all(self, display):

        self.title.blit(display)

        self.choose_dungeon_type_text.blit(display)
