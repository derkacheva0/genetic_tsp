from GUI.gui import *
from GeneticTSP.TSP import *
from Adapter import *
from Reader import *
from Generator import *


class Mediator:

    def __init__(self, window):
        self.window = window
        self.window.set_mediator(self)
        self.tsp = None
        self.logger = None
        self.adapter = Adapter()

    def run(self):

        cities = self.window.sc.get_cities()
        self.adapter.make_adjacency_matrix(cities)

        population_size = self.window.horizontalSlider.value()
        generation_number = self.window.horizontalSlider_2.value()
        mutation_chance = self.window.horizontalSlider_3.value() / 100
        crossing_chance = self.window.horizontalSlider.value() / 100

        self.__initialize_algorithm(self.adapter.get_adjacency_matrix(), generation_number, population_size, mutation_chance, crossing_chance)

        crossover = self.adapter.convert_crossover( self.window.comboBox.currentText(), self.logger)
        mutation = self.adapter.convert_mutation( self.window.comboBox_2.currentText(), self.logger)
        selection = self.adapter.convert_selection( self.window.comboBox_3.currentText() )
        parent_selection = self.adapter.convert_parent_selection( self.window.comboBox_4.currentText() )

        self.tsp.choose_operators(mutation, crossover, selection, parent_selection)
        self.window.population_history = self.tsp.run()
        loggs_history = self.logger.get_loggs()
        self.logger.save_loggs(loggs_history)

    def __initialize_algorithm(self, adjacency_matrix: List[List[float]], generation_number: int, population_size: int, mutation_chance: float, crossover_chance: float):
        self.logger = Logger(generation_number)
        self.tsp = TSP(self.adapter.get_adjacency_matrix(), generation_number, population_size, mutation_chance, crossover_chance, self.logger)

    def generate_data(self):
        gen_cities = Generator().generate_data()
        self.window.sc.set_cities(gen_cities)

    def read_data(self, path):
        file_cities = Reader(path).read_data()
        self.window.sc.set_cities(file_cities)

