import pygame

import pygame


class DungeonDrawer:

    def __init__(self, display):

        self.display = display
    
    def draw_dungeon(self, dungeon):

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