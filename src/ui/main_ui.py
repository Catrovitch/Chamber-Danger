import pygame

from ui.renderer import Renderer
from services.BSPDungeon import BSPDungeon
from services.OrganicBSPDungeon import OrganicBSPDungeon
from .ui_entities.text import Text

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
                            render_dungeon = True


                            print("Node numbers: ")
                            for node in (self.dungeon._nodes):
                                print(f"Parent: {node.node_nr}")
                                try:
                                    print(f"Child1: {node.child_1.node_nr}")
                                except AttributeError:
                                    print(f"Node {node.node_nr} has no child_1")
                                try:
                                    print(f"Child2: {node.child_2.node_nr}")
                                except AttributeError:
                                    print(f"Node {node.node_nr} has no child_2")

                                print("")
                            

                        if self.renderer.organic_tickbox.ticked == True:
                            self.dungeon = OrganicBSPDungeon(dungeon_size, max_chamber_size, min_chamber_size)
                            self.dungeon.generateMap()
                            dungeon_generated = True        
                
                if event.type == pygame.MOUSEBUTTONUP:

                    self.click = False

                    self.renderer.dungeon_sizeline.button.clicked = False
                    

            if dungeon_generated:

                if render_dungeon:
                    self.display.fill((50, 50, 50))
                    self.renderer.render_dungeon_background()
                    self.renderer.render_dungeon(self.dungeon)
                    render_dungeon = False
                
                if show_corridors:
                    for corridor in self.dungeon.corridors:
                        pygame.draw.line(self.display, (20, 20, 20), (corridor.x1*10+4, corridor.y1*10+4), (corridor.x2*10+4, corridor.y2*10+4), 16)
                        pygame.draw.line(self.display, (corridor.colour), (corridor.x1*10+5, corridor.y1*10+5), (corridor.x2*10+5, corridor.y2*10+5), 8)
                if show_chambers:
                    for chamber in self.dungeon.chambers:
                        pygame.draw.rect(self.display, (chamber.colour), (chamber.x1*10, chamber.y1*10, chamber.width*10, chamber.height*10))
                        chamber_number = Text(str(chamber.number), chamber.x1*10, chamber.y1*10, 24)
                        chamber_number.blit(self.display)
                    
                if show_graph:
                    for corridor in self.dungeon.graph_visualizer:
                        pygame.draw.line(self.display, (255,255,255), (corridor.x1*10-1, corridor.y1*10-1), (corridor.x2*10-1, corridor.y2*10-1), 8)
                        pygame.draw.line(self.display, (corridor.colour), (corridor.x1*10, corridor.y1*10), (corridor.x2*10, corridor.y2*10), 5)
                        
            self.renderer.render_all()

            pygame.display.flip()
