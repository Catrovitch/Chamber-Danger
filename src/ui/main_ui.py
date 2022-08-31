import pygame

from ui.renderer import Renderer
from services.BSPDungeon import BSPDungeon
from services.OrganicBSPDungeon import OrganicBSPDungeon


class UI:

    def __init__(self):

        pygame.init()

        height = 800
        width = 1400

        self.display = pygame.display.set_mode((width, height))

        self.renderer = Renderer(self.display)

    def main_loop(self):

        dungeon_generated = False
        show_chambers = False
        render_dungeon = False
        show_corridors = False
        show_graph = False
        show_dungeon_depth = False
        self.click = False

        self.display.fill((50, 50, 50))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                pos = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:

                    self.click = True

                    if self.renderer.industrial_tickbox.is_clicked(pos):
                        self.renderer.industrial_tickbox.ticked = True
                        self.renderer.organic_tickbox.ticked = False

                    if self.renderer.organic_tickbox.is_clicked(pos):
                        self.renderer.organic_tickbox.ticked = True
                        self.renderer.industrial_tickbox.ticked = False

                    if self.renderer.chambers_tickbox.is_clicked(pos):

                        if self.renderer.chambers_tickbox.ticked == False:
                            self.renderer.chambers_tickbox.ticked = True
                            show_chambers = True

                        elif self.renderer.chambers_tickbox.ticked == True:
                            self.renderer.chambers_tickbox.ticked = False
                            show_chambers = False
                            render_dungeon = True

                    if self.renderer.corridors_tickbox.is_clicked(pos):

                        if self.renderer.corridors_tickbox.ticked == False:
                            self.renderer.corridors_tickbox.ticked = True
                            show_corridors = True

                        elif self.renderer.corridors_tickbox.ticked == True:
                            self.renderer.corridors_tickbox.ticked = False
                            show_corridors = False
                            render_dungeon = True

                    if self.renderer.graph_tickbox.is_clicked(pos):

                        if self.renderer.graph_tickbox.ticked == False:
                            self.renderer.graph_tickbox.ticked = True
                            show_graph = True

                        elif self.renderer.graph_tickbox.ticked == True:
                            self.renderer.graph_tickbox.ticked = False
                            show_graph = False
                            render_dungeon = True

                    if self.renderer.dungeon_depth.is_clicked(pos):

                        if self.renderer.dungeon_depth.ticked == False:
                            self.renderer.dungeon_depth.ticked = True
                            show_dungeon_depth = True

                        elif self.renderer.dungeon_depth.ticked == True:
                            self.renderer.dungeon_depth.ticked = False
                            show_dungeon_depth = False
                            render_dungeon = True

                    self.renderer.dungeon_sizeline.update_button_and_size(pos)

                    self.renderer.max_chamber_size_sizeline.update_button_and_size(
                        pos)

                    self.renderer.min_chamber_size_sizeline.update_button_and_size(
                        pos)

                    if self.renderer.generate_dungeon_button.is_clicked(pos):

                        dungeon_size = self.renderer.dungeon_sizeline.size
                        max_chamber_size = self.renderer.max_chamber_size_sizeline.size
                        min_chamber_size = self.renderer.min_chamber_size_sizeline.size

                        if self.renderer.industrial_tickbox.ticked == True:

                            self.dungeon = BSPDungeon(
                                dungeon_size, max_chamber_size, min_chamber_size)
                            self.dungeon.generateMap()
                            dungeon_generated = True
                            render_dungeon = True

                        if self.renderer.organic_tickbox.ticked == True:
                            self.dungeon = OrganicBSPDungeon(
                                dungeon_size, max_chamber_size, min_chamber_size)
                            self.dungeon.generateMap()
                            dungeon_generated = True
                            render_dungeon = True

                if event.type == pygame.MOUSEBUTTONUP:

                    self.click = False

                    self.renderer.dungeon_sizeline.button.clicked = False

            if dungeon_generated:

                if render_dungeon:
                    self.display.fill((50, 50, 50))
                    self.renderer.render_dungeon_background()
                    self.renderer.render_dungeon(self.dungeon)
                    render_dungeon = False

                if show_dungeon_depth and self.renderer.dungeon_depth.ticked:
                    self.renderer.render_depth_level_chambers(self.dungeon)

                if show_corridors and self.renderer.industrial_tickbox.ticked:
                    self.renderer.render_corridors(self.dungeon)

                if show_corridors and self.renderer.organic_tickbox.ticked:
                    self.renderer.render_drunkardswalk(self.dungeon)

                if show_chambers:
                    self.renderer.render_chambers(self.dungeon)

                if show_graph:
                    self.renderer.render_graph(self.dungeon)

            self.renderer.render_all()

            pygame.display.flip()
