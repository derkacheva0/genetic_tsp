from GeneticTSP.Strategy.Interfaces import *


class RandomSelection(ISelection):
    """
    Особи выбираются случайным образом без учета их приспособленности 
    """
    def execute(self, population: Population) -> None:

        while len(population.get()) > population.get_max_number():
            random_individual = random.choice( list(population.get()) ) 
            fitness = population.get()[random_individual]
            population.remove(random_individual, fitness)


class EliteSelection(ISelection):
    """
    Лучшие особи из текущей популяции непосредственно передаются 
        в следующее поколение.
    В данном случае, только 10 % элитных особей идут в новое поколение. Остальные
        отбираются случайно
    """
    def execute(self, population: Population) -> None:
        if len(population.get()) < population.get_max_number():
            return

        sorted_population = dict(
                sorted(population.get().items(), key=lambda item: item[1])
                )

        population.set({})
        elite_individuals_percent = 0.1

        for i, key in enumerate(sorted_population):
            if i <= (elite_individuals_percent * len(sorted_population)):
                population.add(key, sorted_population[key])
            else:
                random_individual = random.choice( list(sorted_population) )
                population.add(random_individual, sorted_population[random_individual])
            if i > population.get_max_number():
                break
                

class ExclusionSelection(ISelection):
    """
    Выбираем наиболее различные особи для нового поколения
    """
    def execute(self, population: Population) -> None:
        if len(population.get()) < population.get_max_number():
            return
        new_population = {}
        selection_coefficient = 0.4

        for first_individual in population.get():
            if len(new_population) >= population.get_max_number():
                break
            fitness1 = population.calculate_fitness(first_individual)
            new_population.update({first_individual: fitness1})

            for second_individual in population.get():
                different_genes = self.__different_genes_amount(first_individual, second_individual)
                if different_genes >= (selection_coefficient * len(first_individual)):
                    fitness2 = population.calculate_fitness(second_individual)
                    new_population.update({second_individual: fitness2})

                if len(new_population) >= population.get_max_number():
                    break
        population.set(new_population)

    def __different_genes_amount(self, first_individual: Tuple[int, ...], second_individual: Tuple[int, ...]) -> int:
        counter = len(first_individual)
        for i in range(len(first_individual)):
            if first_individual[i] == second_individual[i]:
                counter -= 1
        return counter


