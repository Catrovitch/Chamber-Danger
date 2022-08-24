from services.BSPDungeon import BSPDungeon
from services.OrganicBSPDungeon import OrganicBSPDungeon


class UiService():

    def __init__(self):

        pass

    
    def dungeon_type_and_size(self):

        dungeon_type = None

        map_height = 8
        map_width = 10

        while True:
            dungeon_type = input(
                "What type of dungeon should be generated? (1 for constructed, 2 for organic) ")

            if (dungeon_type) in ("1", "2"):
                break

        while True:
            map_size = input("Give dungeon size (1-10): ")

            try:
                map_size = int(map_size)
            except:
                continue
            
            if 1 <= map_size <= 10:
                break
           
        map_height *= map_size
        map_width *= map_size

        if dungeon_type == "1":

            dungeon = BSPDungeon()
            dungeon.generateMap(map_width, map_height)

        if dungeon_type == "2":

            dungeon = OrganicBSPDungeon()
            dungeon.generateMap(map_width, map_height)

        self.dungeon = dungeon