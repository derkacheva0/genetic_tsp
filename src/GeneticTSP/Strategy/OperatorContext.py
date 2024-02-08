from GeneticTSP.Strategy.Interfaces import *


class OperatorContext():
    
    def __init__(self):
        self.mutation_strategy = None
        self.selection_strategy = None
        self.crossover_strategy = None
        self.parent_selection_strategy = None

    def selection(self, population: Population) -> None:
        if self.selection_strategy is not None:
            self.selection_strategy.execute(population)

    def crossover(self, population: Population, rates: Rates) -> None:
        if (self.crossover_strategy is not None and 
            self.parent_selection_strategy is not None and
            self.mutation_strategy is not None
            ):
            
            self.crossover_strategy.execute(self.parent_selection_strategy, self.mutation_strategy, population, rates)
    
    def choose_mutation(self, mutation_strategy: IMutation) -> None:
        self.mutation_strategy = mutation_strategy

    def choose_selection(self, selection_strategy: ISelection) -> None:
        self.selection_strategy = selection_strategy

    def choose_crossover(self, crossover_strategy: ICrossover) -> None:
        self.crossover_strategy = crossover_strategy
    
    def choose_parent_selection(self, parent_selection_strategy: IParentSelection):
        self.parent_selection_strategy = parent_selection_strategy
