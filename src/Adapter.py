from dataclasses import dataclass
from math import sqrt
from typing import List, Tuple

from GeneticTSP.Strategy.Strategies.Mutations import *
from GeneticTSP.Strategy.Strategies.Crossovers import *
from GeneticTSP.Strategy.Strategies.Selections import *
from GeneticTSP.Strategy.Strategies.ParentSelections import *
from GeneticTSP.Logger import *


class Adapter:
    """
    Данный класс нужен для связи между GUI и самим алгоритмом. Он работает со
    всеми вершинами в графе, выбранными пользователем. Способен составить матрицу
    смежности для получившегося полного графа.
    """
    def __init__(self):
        self.adjacency_matrix = []

    def get_adjacency_matrix(self) -> List[List[float]]:
        return self.adjacency_matrix

    def make_adjacency_matrix(self, node_set: List[List[float]]) -> None:
        
        self.adjacency_matrix = [[] for _ in range(len(node_set))]

        for i in range(len(node_set)):

            for j in range(len(node_set)):
                distance = self.__euclidean_distance(tuple(node_set[i]), tuple(node_set[j]))
                self.adjacency_matrix[i].append(distance)

    def __euclidean_distance(self, node1: Tuple[float, float], node2: Tuple[float, float]) -> float:
        """
        Находит евклидово расстояние между двумя точками в двумерном пространстве.
        """
        x1, y1 = node1
        x2, y2 = node2
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def convert_mutation(self, mutation: str, logger: Logger):
        if mutation == "SwapMutation":
            return SwapMutation(logger)
        elif mutation == "UniformMutation":
            return UniformMutation(logger)
        elif mutation == "ScrambleMutation":
            return ScrambleMutation(logger)
        else:
            raise NameError(f"Mutation Class {mutation} does not exist")

    def convert_crossover(self, crossover: str, logger: Logger):
        if crossover == "SinglePointCrossover":
            return SinglePointCrossover(logger)
        elif crossover == "TwoPointCrossover":
            return TwoPointCrossover(logger)
        elif crossover == "UniformCrossover":
            return UniformCrossover(logger)
        else:
            raise NameError(f"Crossover Class {crossover} does not exist")

    def convert_parent_selection(self, parent_selection: str):
        if parent_selection == "Panmixia":
            return Panmixia()
        elif parent_selection == "TournamentParentSelection":
            return TournamentParentSelection()
        elif parent_selection == "RoulleteWheelParentSelection":
            return RoulleteWheelParentSelection()
        else:
            raise NameError(f"ParentSelection Class {parent_selection} does not exist")

    def convert_selection(self, selection: str):
        if selection == "RandomSelection":
            return RandomSelection()
        elif selection == "EliteSelection":
            return EliteSelection()
        elif selection == "ExclusionSelection":
            return ExclusionSelection()
        else:
            raise NameError(f"Selection Class {selection} does not exist")
