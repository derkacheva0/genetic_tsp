from GeneticTSP.Population import *


class Caretaker:
    def __init__(self):
        self.population_history = []

    def save(self, population: Population) -> None:
        self.population_history.append(population.get())
        
    def get_history(self):
        return self.population_history
    
