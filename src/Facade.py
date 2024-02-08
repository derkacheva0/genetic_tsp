from GeneticTSP.Strategy.Strategies.Mutations import *
from GeneticTSP.Strategy.Strategies.Crossovers import *
from GeneticTSP.Strategy.Strategies.Selections import *
from GeneticTSP.TSP import *

from GUI.gui import *


class Facade:

    def __init__(self):
        self.gui = GUI()
        self.tsp = None
        pass

    def run(self):
        while self.gui.get_ui().ready != 1:
            pass
        cities = self.gui.get_ui().sc.get_cities()
        #print(cities)
        population_size = int(self.gui.get_ui().lineEdit_X.text())
        generation_number = int(self.gui.get_ui().lineEdit_X_2.text())
        mutation_chance = float(self.gui.get_ui().lineEdit_X_3.text())
        crossing_chance = float(self.gui.get_ui().lineEdit_X_4.text())
        #print(population_size, generation_number, mutation_chance, crossing_chance)
