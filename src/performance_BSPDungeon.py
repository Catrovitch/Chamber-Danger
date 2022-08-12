from json.encoder import INFINITY
from matplotlib import pyplot as plt
import time
from services.BSPDungeon import BSPDungeon


class PerformanceBSPDungeon():

    def __init__(self):

        self.dungeon = BSPDungeon()

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

            self.dungeon = BSPDungeon()

        average = aggregated_time/self.iterations

        n = width*height

        self.size.append(n)
        self.best.append(quickest)
        self.worst.append(slowest)
        self.average.append(average)

    def make_plot(self):

        plt.plot(self.size, self.average, color= "blue")
        plt.plot(self.size, self.worst, color= "red")
        plt.plot(self.size, self.best, color="green")
        plt.title(f"Best (green), worst (red) and average (blue) execution-time for BFSDungeon_generation of all dungeon sizes\nDone with a {self.iterations} iterations", fontsize=14)
        plt.xlabel("Amount of individual tiles in dungeon", fontsize=14)
        plt.ylabel("Execution-time", fontsize=14)
        plt.grid(True)
        plt.show()


if __name__=="__main__":

    performance_bspdungeon = PerformanceBSPDungeon()

    performance_bspdungeon.execute_test()
