from services.ui_service import UiService
from ui.draw_dungeon import draw_dungeon


def generate_dungeon():

    ui = UiService()
    ui.dungeon_type_and_size()
    draw_dungeon(ui.dungeon, ui.dungeon.map_height, ui.dungeon.map_width)


if __name__ == "__main__":

    generate_dungeon()