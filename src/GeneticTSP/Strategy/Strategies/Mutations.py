from GeneticTSP.Strategy.Interfaces import *

class SwapMutation(IMutation):
    """!
    Выбираем в популяции случайную особь и меняем у нее два случайных гена местами. 
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        mutant = list(individual[:-1])
        idx1, idx2 = random.sample(range(len(mutant)), 2)
        mutant[idx1], mutant[idx2] = mutant[idx2], mutant[idx1]
        mutant.append(mutant[0])

        self.logger.add_log(self, individual, mutant)

        return tuple(mutant)


class UniformMutation(IMutation):
    """!
    При равномерной мутации каждая позиция в особи имеет небольшую 
        вероятность быть измененной.
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        not_seen = list(individual[:-1])
        mutant = []
        gene_mutation_chance = 0.4
        for gene in individual[:-1]:
            random_chance = random.uniform(0, 1)
            if random_chance < gene_mutation_chance or gene not in not_seen:
                random_gene = random.choice( not_seen )
                mutant.append(random_gene)
                not_seen.remove(random_gene)
            else:
                mutant.append(gene)
                not_seen.remove(gene)
        mutant.append(mutant[0])

        self.logger.add_log(self, individual, mutant)

        return tuple(mutant)


class ScrambleMutation(IMutation):
    """!
    Выбираются две случайные позиции в особи, и гены между этими 
        позициями перемешиваются случайным образом.
    """
    def __init__(self, logger: Logger):
        self.logger = logger

    def execute(self, individual: Tuple[int, ...]) -> Tuple[int, ...]:
        mutant = list(individual[:-1])
        idx1, idx2 = random.sample(range(len(mutant)), 2)

        start_idx = min(idx1, idx2)
        end_idx = max(idx1, idx2)
        if start_idx == end_idx:
            return individual

        subsequence = mutant[start_idx + 1:end_idx]

        random.shuffle(subsequence)

        mutant = mutant[:start_idx + 1] + subsequence + mutant[end_idx:]
        mutant = list(set(mutant))
        mutant.append(mutant[0])

        self.logger.add_log(self, individual, mutant)

        return tuple(mutant)

