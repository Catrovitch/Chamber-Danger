from services.dungeon import Dungeon
from ui.draw_dungeon import draw_dungeon
from ui.draw_dungeon2 import draw_dungeon2


def generate_dungeon():    
    dungeon = Dungeon()
    dungeon.create_map()
    dungeon.create_rooms()
    dungeon.connect_rooms()

    draw_dungeon(dungeon.map)

    
    
if __name__ == "__main__":
    generate_dungeon()