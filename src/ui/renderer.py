import pygame

from ui.ui_entities.size_line import Sizeline
from ui.text_holder import TextHolder
from ui.tick_box import TickBox
from ui.ui_entities.button import Button


class Renderer:

    def __init__(self, display):

        self.display = display

        self.textholder = TextHolder()

        self.industrial_tickbox = TickBox(1280, 148, "Industrial dungeon: ")
        self.organic_tickbox = TickBox(1280, 178, "Organic dungeon: ")

        self.dungeon_sizeline = Sizeline(1080, 1320, 420, "Choose dungeon size:", (15, 35))
        self.min_chamber_size_sizeline = Sizeline(1080, 1320, 520, "Min chamber size", (2, 6))
        self.max_chamber_size_sizeline = Sizeline(1080, 1320, 620, "Max chamber size:", (7, 20))


        self.generate_dungeon_button = Button(1080, 660, 240, 50, "Generate dungeon")

    def render_menu_background(self):

        colour = (80, 80, 80)
        x = 1050
        y = 30
        width = 300
        height = 700    

        pygame.draw.rect(self.display, (43, 20, 20), (x-15, y-15, width+30, height + 30))
        pygame.draw.rect(self.display, colour, (x, y, width, height))

    def render_dungeon_background(self):

        colour = (50, 50, 50)

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
        self.max_chamber_size_sizeline.render(self.display)
        self.min_chamber_size_sizeline.render(self.display)


    def render_generate_dungeon_button(self):

        self.generate_dungeon_button.render(self.display)

    def render_dungeon(self, dungeon):

        wall_colour = (50, 50, 50)
        chamber_colour = (145, 88, 88)

        square_x = 0
        square_y = 0
        
        for y in range(dungeon.map_height):
            for x in range(dungeon.map_width):
                if int(dungeon.map[x][y]) == 1:
                    pygame.draw.rect(
                        self.display, wall_colour, (square_x, square_y, square_x+10, square_y+10))
                    square_x += 10

                else:
                    pygame.draw.rect(
                        self.display, chamber_colour, (square_x, square_y, square_x+10, square_y+10))
                    square_x += 10

            square_y += 10
            square_x = 0


    def render_all(self):

        self.render_menu_background()
        self.render_all_text()
        self.render_tickboxes()
        self.render_dungeon_sizeline()
        self.render_generate_dungeon_button()
