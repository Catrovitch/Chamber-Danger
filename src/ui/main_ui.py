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
                        

                    self.renderer.dungeon_sizeline.update_button_and_size(pos)

                    self.renderer.max_chamber_size_sizeline.update_button_and_size(pos)

                    self.renderer.min_chamber_size_sizeline.update_button_and_size(pos)


                    if self.renderer.generate_dungeon_button.is_clicked(pos):

                        dungeon_size = self.renderer.dungeon_sizeline.size
                        max_chamber_size = self.renderer.max_chamber_size_sizeline.size
                        min_chamber_size = self.renderer.min_chamber_size_sizeline.size


                        if self.renderer.industrial_tickbox.ticked == True:

                            self.dungeon = BSPDungeon(dungeon_size, max_chamber_size, min_chamber_size)
                            self.dungeon.generateMap()
                            dungeon_generated = True

                        if self.renderer.organic_tickbox.ticked == True:
                            self.dungeon = OrganicBSPDungeon(dungeon_size, max_chamber_size, min_chamber_size)
                            self.dungeon.generateMap()
                            dungeon_generated = True        
                
                if event.type == pygame.MOUSEBUTTONUP:

                    self.click = False

                    self.renderer.dungeon_sizeline.button.clicked = False
                    


            if dungeon_generated:
                self.renderer.render_dungeon_background()
                self.renderer.render_dungeon(self.dungeon)
                pygame.display.flip()
                dungeon_generated = False


            self.renderer.render_all()

            pygame.display.flip()
