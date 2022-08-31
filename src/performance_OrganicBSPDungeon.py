from json.encoder import INFINITY
from matplotlib import pyplot as plt
import time

from services.OrganicBSPDungeon import OrganicBSPDungeon


class PerformanceBSPDungeon():

    def __init__(self):

        self.dungeon = OrganicBSPDungeon()

        self.size = []
        self.best = []
        self.worst = []
        self.average = []

    def execute_test(self):

        for i in range(1, 11):
            self.test(i)

        self.make_plot()
 

    def test(self, size):

        aggregated_time = 0
        quickest = INFINITY
        slowest = 0
        average = 0

        width = 10*size
        height = 8*size

        self.iterations = 100

        for i in range(self.iterations):

            start = time.time()

            self.dungeon.generateMap(width, height)

            end = time.time()

            execution_time = end-start

            if execution_time < quickest:
                quickest = execution_time

            if execution_time > slowest:
                slowest = execution_time

            aggregated_time += execution_time

            self.dungeon = OrganicBSPDungeon()

        average = aggregated_time/self.iterations

        n = width*height

        self.size.append(n)
        self.best.append(quickest)
        self.worst.append(slowest)
        self.average.append(average)

    def make_plot(self):

        plt.plot(self.size, self.worst, color= "red", label = "worst")
        plt.plot(self.size, self.average, color= "blue", label = "average")
        plt.plot(self.size, self.best, color="green", label = "best")
        plt.title(f"Execution-time for OrganicBSPDungeon_generation of all dungeon sizes\nDone with a {self.iterations} iterations", fontsize=14)
        plt.xlabel("Amount of individual tiles in dungeon", fontsize=14)
        plt.ylabel("Execution-time", fontsize=14)
        plt.grid(True)
        plt.legend()
        plt.savefig('./documentation/pictures/OrganicBSPDungeon_performance_test.png', transparent=False, dpi=80, bbox_inches="tight")


