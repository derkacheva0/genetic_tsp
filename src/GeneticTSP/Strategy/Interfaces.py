from GeneticTSP.Population import *
from GeneticTSP.Structures import *
from GeneticTSP.Logger import *

from typing import Protocol, Tuple, List
import random


class IMutation(Protocol):
    def __init__(self, logger: Logger):
        pass

    def execute(self, individual: Tuple[int, ...]):
        """
        Оператор мутации -- замена некоторого числа генов какой-то особи
        """
        pass


class IParentSelection(Protocol):
    def execute(self, population: Population): 
        """
        Оператор выбора родителей для дальнейшего скрещивания
        """
        pass


class ICrossover(Protocol):
    def __init__(self, logger: Logger):
        pass

    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        """ 
        Оператор скрещивания -- 'шафл' генов у некоторого числа особей
        """
        pass

    def _try_to_mutate(self, individual: Tuple[int, ...], mutation: IMutation, rates: Rates) -> Tuple[int, ...]:
        mutate_chance = random.uniform(0, 1)
        if mutate_chance < rates.mutation:
            return mutation.execute(individual)
        return individual


class ISelection(Protocol):
    def execute(self, population: Population) -> None:
        """
        Оператор селекции -- правило отбора особей внутри популяции
        """
        pass

