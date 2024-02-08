from GeneticTSP.Caretaker import *
from GeneticTSP.Strategy.OperatorContext import * 
from GeneticTSP.Structures import *


class TSP:
    def __init__(self, adjacency_matrix: List[List[float]], 
                 generations_number: int, population_max_number: int,
                 mutation_rate: float, crossover_rate: float, logger):
        self.population = Population(adjacency_matrix, population_max_number, generations_number)
        self.rates = Rates(mutation_rate, crossover_rate)
        self.caretaker = Caretaker()
        self.operator_context = OperatorContext()
        self.logger = logger

    def run(self) -> List[Dict[Tuple[int, ...], float]]:
        self.population.generate_random_population()
        for _ in range(self.population.get_generations_number()):
            self.operator_context.crossover(self.population, self.rates)
            self.caretaker.save(self.population)
            self.operator_context.selection(self.population)
            self.logger.next_generation()
        return self.caretaker.get_history()

    def choose_operators(self, mutation: IMutation, 
                         crossover: ICrossover, 
                         selection: ISelection,
                         parent_selection: IParentSelection,
                        ) -> None:
        """
        Выбораем конкретные операторы мутации, кроссовера и селекции
        """
        self.operator_context.choose_mutation(mutation)
        self.operator_context.choose_crossover(crossover)
        self.operator_context.choose_selection(selection)
        self.operator_context.choose_parent_selection(parent_selection)


