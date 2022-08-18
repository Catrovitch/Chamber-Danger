import pygame


def draw_dungeon(dungeon, map_height, map_width):

    pygame.init()

    height = map_height*10
    width = map_width*10

    window = pygame.display.set_mode((width, height))

    wall_colour = (0, 0, 0)
    chamber_colour = (92, 92, 92)

    clock = pygame.time.Clock()

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

        clock.tick(1)
