from services.ui_service import UiService
from ui.draw_dungeon import draw_dungeon


def generate_dungeon():

    ui = UiService()
    ui.dungeon_type()
    draw_dungeon(ui.dungeon)


if __name__ == "__main__":
    generate_dungeon()
