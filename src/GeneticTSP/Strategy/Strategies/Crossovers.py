from GeneticTSP.Strategy.Interfaces import *


class SinglePointCrossover(ICrossover):
    """
    До некоторого гена-маркера, родители обмениваются цепочками генов, 
        тем самым порождая двух потомков
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)
        
        marker = random.randint(1, len(parent1[:-1]) - 1)

        child1 = parent1[:marker] + parent2[marker:]
        child2 = parent2[:marker] + parent1[marker:]

        child1 = self.__individual_validation(child1)
        child2 = self.__individual_validation(child2)

        child1 = self._try_to_mutate(child1, mutation, rates)
        child2 = self._try_to_mutate(child2, mutation, rates)

        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)

        self.logger.add_log(self, parent1, parent2, child1, child2, population)

        population.add(child1, fitness1)
        population.add(child2, fitness2)

    def __individual_validation(self, child: Tuple[int, ...]) -> Tuple[int, ...]:
        gene_set = [i for i in range(len(child) - 1)]
        better_child = [gene for gene in child if child.count(gene) == 1]
        while len(better_child) < len(gene_set):
            random_gene = random.choice( gene_set )
            if random_gene not in better_child:
                better_child.append(random_gene)
        better_child.append(better_child[0])
        return tuple(better_child)


class TwoPointCrossover(ICrossover):
    """
    Этот вид скрещивания аналогичен одноточечному скрещиванию, но 
        в данном случае может происходить обмен генами в нескольких 
        случайно выбранных точках особи (В данном случае точки 2).
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

        crossover_markers = random.sample(range(1, len(parent1[:-1])), 2)
        crossover_markers.sort()

        child1 = self.__create_child(parent1, parent2, crossover_markers)
        child2 = self.__create_child(parent2, parent1, crossover_markers)
        
        child1 = self._try_to_mutate(tuple(child1), mutation, rates)
        child2 = self._try_to_mutate(tuple(child1), mutation, rates)
        
        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)
        
        self.logger.add_log(self, parent1, parent2, child1, child2, population)
        
        population.add(child1, fitness1)
        population.add(child2, fitness2)

    def __create_child(self, parent1, parent2, crossover_points):
        middle_part = parent2[crossover_points[0]:crossover_points[1]]
        end_part = parent1[crossover_points[1]:]
    
        child = list(parent1[:crossover_points[0]])
        not_seen = [i for i in range(len(parent1) - 1) if (i not in child and i not in end_part)]
        for gene in middle_part:
            if gene not in child and gene not in end_part:
                not_seen.remove(gene)
                child.append(gene)
            else:
                random_gene = random.choice(not_seen)
                not_seen.remove(random_gene)
                child.append(random_gene)
        child = child + list(end_part)
        return tuple(child)


class UniformCrossover(ICrossover):
    """
    При равномерном скрещивании каждый ген в потомке выбирается 
        случайным образом от одного из родителей.
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, parent_selection: IParentSelection, mutation: IMutation, population: Population, rates: Rates) -> None:
        parent1, parent2 = parent_selection.execute(population)

        child1 = [None] * len(parent1)
        child2 = [None] * len(parent2)

        not_seen_child1 = [i for i in range(len(child1) - 1)]
        not_seen_child2 = [i for i in range(len(child2) - 1)]
        for i in range(len(parent1) - 1):
            self.__try_to_swap(parent1, parent2, child1, i, not_seen_child1)
            self.__try_to_swap(parent1, parent2, child2, i, not_seen_child2)
        child1[-1] = child1[0]
        child2[-1] = child2[0]

        child1 = self._try_to_mutate(tuple(child1), mutation, rates)
        child2 = self._try_to_mutate(tuple(child2), mutation, rates)

        fitness1 = population.calculate_fitness(child1)
        fitness2 = population.calculate_fitness(child2)

        self.logger.add_log(self, parent1, parent2, child1, child2, population)

        population.add(child1, fitness1)
        population.add(child2, fitness2)

    def __try_to_swap(self, parent1, parent2, child, i, not_seen):
        if parent1[i] not in child and parent2[i] not in child:
            coin_flip = random.randint(0, 1)
            if coin_flip == 0:
                child[i] = parent1[i]
            else:
                child[i] = parent2[i]
        elif parent1[i] not in child and parent2[i] in child:
            child[i] = parent1[i]
        elif parent1[i] in child and parent2[i] not in child:
            child[i] = parent2[i]
        else:
            child[i] = random.choice(not_seen)
        not_seen.remove(child[i])
