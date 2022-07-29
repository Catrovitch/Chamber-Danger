import pygame
from random import randrange

def draw_dungeon(map_dic):
    """Draw the dungeon with cario rectangles."""    
    pygame.init()

    window = pygame.display.set_mode((500, 500))

    wall_colour = (0, 0, 0)
    room_colour = (92, 92, 92)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            square_x = 0
            square_y = 0

            for y in range(50):
                for x in range(50):
                    
                    if map_dic[x,y] == 0:
                        pygame.draw.rect(window, wall_colour, (square_x, square_y, square_x+10, square_y+10))
                        square_x += 10
                    
                    else:
                        pygame.draw.rect(window, room_colour, (square_x, square_y, square_x+10, square_y+10))
                        square_x += 10

                square_y += 10
                square_x = 0

        pygame.display.flip()