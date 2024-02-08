from GeneticTSP.Strategy.Interfaces import *


class Panmixia(IParentSelection):
    """!
    Панмиксия — оба родителя выбираются случайно, 
        каждая особь популяции имеет равные шансы быть выбранной
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
        return tuple(population.get_random_individuals(2))


class TournamentParentSelection(IParentSelection):
    """!
    Турнирная селекция — сначала случайно выбирается установленное количество 
        особей, а затем из них выбирается особь с лучшим значением функции приспособленности
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]: 
        winners = []
        while len(winners) < 2:
            challenger1, challenger2 = population.get_random_individuals(2)
            fitness1, fitness2 = population.get()[challenger1], population.get()[challenger2]
            if fitness1 > fitness2:
                winners.append(challenger1)
            else:
                winners.append(challenger2)
        return tuple(winners)


class RoulleteWheelParentSelection(IParentSelection):
    """!
    Особи выбираются пропорционально их приспособленности. 
        Более приспособленные особи имеют больший шанс быть выбранными, 
        поскольку их приспособленность увеличивает их долю на колесе рулетки
    """
    def execute(self, population: Population) -> Tuple[Tuple[int, ...], Tuple[int, ...]]: 
        average_value = sum(population.get().values())
        winners = []

        while len(winners) < 2:
            random_individual = random.choice( list(population.get()) )
            fitness = population.get()[random_individual]

            random_chance = random.uniform(0, 1)
            if random_chance < (fitness / average_value):
                winners.append(random_individual)

        return tuple(winners)


