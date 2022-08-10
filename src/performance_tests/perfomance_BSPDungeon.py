import cProfile
from ..services.BSPDungeon import BSPDungeon


class PerformanceBSPDungeon():

    def __init__(self):

        self.dungeon = BSPDungeon()


    def test(self):

        height = 25
        width = 40

        cProfile.run(self.dungeon.generateMap(width, height))


if __name__=="__main__":

    performance_bspdungeon = PerformanceBSPDungeon()

    performance_bspdungeon.test()


