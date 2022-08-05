from services.BSPDungeon import BSPDungeon
from services.OrganicBSPDungeon import OrganicBSPDungeon


class UiService():

    def __init__(self):

        pass

    def dungeon_type(self):

        dungeon_type = None

        while True:
            dungeon_type = input(
                "What type of dungeon should be generated? (1 for constructed, 2 for organic) ")

            if (dungeon_type) in ("0", "1", "2"):
                break

        if dungeon_type == "1":

            self.BSPDungeon()

        if dungeon_type == "2":

            self.OrganicBSPDungeon()

    def BSPDungeon(self):

        map_height = 1000
        map_width = 1000

        while True:
            map_height = input("Give map height (25-70): ")
            try:
                map_height = int(map_height)
            except:
                continue

            if 25 <= map_height <= 70:
                break

        while True:
            map_width = input("Give map width (40-100): ")
            try:
                map_width = int(map_width)
            except:
                continue

            if 40 <= map_width <= 100:
                break

        dungeon = BSPDungeon()
        dungeon.generateMap(map_width, map_height)

        self.dungeon = dungeon

    def OrganicBSPDungeon(self):

        map_height = 1000
        map_width = 1000

        while True:
            map_height = int(input("Give map height (40-70): "))
            try:
                map_height = int(map_height)
            except:
                continue
            if 25 <= map_height <= 70:
                break

        while True:
            map_width = int(input("Give map width (40-100): "))
            try:
                map_width = int(map_width)
            except:
                continue
            if 40 <= map_width <= 100:
                break

        dungeon = OrganicBSPDungeon()
        dungeon.generateMap(map_width, map_height)

        self.dungeon = dungeon
