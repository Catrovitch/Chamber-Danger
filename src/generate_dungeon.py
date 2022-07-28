from dungeon import Dungeon
from draw_dungeon import draw_dungeon

def generate_dungeon():    
    dungeon = Dungeon()
    dungeon.create_map()
    dungeon.create_rooms()
    dungeon.connect_rooms()

    draw_dungeon(dungeon.map)

    
    
if __name__ == "__main__":
    generate_dungeon()