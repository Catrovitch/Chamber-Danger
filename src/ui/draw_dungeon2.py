import pygame
from random import randrange

def draw_dungeon2(room_list):
    """Draw the dungeon with cario rectangles."""    
    pygame.init()

    window = pygame.display.set_mode((500, 500))

    wall_colour = (0, 0, 0)
    room_colour = (92, 92, 92)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            for room in room_list:

                    pygame.draw.rect(window, room_colour, (room.x1, room.y1, room.x2, room.y2))


        pygame.display.flip()