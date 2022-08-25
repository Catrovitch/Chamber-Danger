import pygame

from ui.menu import Menu
from ui.dungeon_drawer import DungeonDrawer
from services.BSPDungeon import BSPDungeon
from services.OrganicBSPDungeon import OrganicBSPDungeon

class UI:

    def __init__(self):

        pygame.init()

        height = 800
        width = 1400

        self.display = pygame.display.set_mode((width, height))

        self.menu = Menu(self.display)
        self.dungeon_drawer = DungeonDrawer(self.display)

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
                    

                    if self.menu.industrial_tickbox.is_clicked(pos):
                        self.menu.industrial_tickbox.ticked = True
                        self.menu.organic_tickbox.ticked = False

                    if self.menu.organic_tickbox.is_clicked(pos):
                        self.menu.organic_tickbox.ticked = True
                        self.menu.industrial_tickbox.ticked = False
                        

                    self.menu.dungeon_sizeline.update_button_and_size(pos)


                    if self.menu.generate_dungeon_button.is_clicked(pos):

                        map_height = 8*self.menu.dungeon_sizeline.size
                        map_width = 10*self.menu.dungeon_sizeline.size

                        if self.menu.industrial_tickbox.ticked == True:
                            self.dungeon = BSPDungeon()
                            self.dungeon.generateMap(map_width, map_height)
                            dungeon_generated = True

                        if self.menu.organic_tickbox.ticked == True:
                            self.dungeon = OrganicBSPDungeon()
                            self.dungeon.generateMap(map_width, map_height)
                            dungeon_generated = True        
                
                if event.type == pygame.MOUSEBUTTONUP:

                    self.click = False


                    self.menu.dungeon_sizeline.button.clicked = False
                    


            if dungeon_generated:
                self.dungeon_drawer.draw_dungeon(self.dungeon)
                pygame.display.flip()
                dungeon_generated = False


            self.menu.render_all()

            pygame.display.flip()








    
            