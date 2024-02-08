from dataclasses import dataclass


@dataclass
class Rates:
    mutation: float = 0.1
    crossover: float = 0.75

    def __post_init__(self):
        if self.mutation < 0 or self.mutation > 1:
            self.mutation = 0.1
        if self.crossover < 0 or self.crossover > 1:
            self.crossover = 0.75


