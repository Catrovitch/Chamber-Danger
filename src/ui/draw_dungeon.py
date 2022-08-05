import pygame


def draw_dungeon(dungeon):

    pygame.init()

    window = pygame.display.set_mode((1000, 700))

    wall_colour = (0, 0, 0)
    chamber_colour = (92, 92, 92)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            square_x = 0
            square_y = 0
            for y in range(dungeon.map_height):
                for x in range(dungeon.map_width):
                    if dungeon.map[x][y] == 1:
                        pygame.draw.rect(
                            window, wall_colour, (square_x, square_y, square_x+10, square_y+10))
                        square_x += 10

                    else:
                        pygame.draw.rect(
                            window, chamber_colour, (square_x, square_y, square_x+10, square_y+10))
                        square_x += 10

                square_y += 10
                square_x = 0

        pygame.display.flip()
