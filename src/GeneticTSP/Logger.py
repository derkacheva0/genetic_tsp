from typing import List


class Logger:
    def __init__(self, generations_number: int):
        self.loggs = [[] for _ in range(generations_number)]
        self.current_generation = 0
        
    def get_loggs(self) -> List[List[str]]:
        return self.loggs

    def save_loggs(self, loggs):
        with open('txt-files/logs.txt', 'w') as file:
            for log in loggs:
                log_line = ','.join(log)
                file.write(log_line + '\n')
    
    def next_generation(self):
        self.current_generation += 1

    def add_log(self, operator, *args, **kwargs):
        if type(operator).__base__.__name__ == "IMutation":
            self.__mutation_log(operator, *args)
        elif type(operator).__base__.__name__ == "ICrossover":
            self.__crossover_log(operator, *args)
    
    def __mutation_log(self, operator, *args):
        individual, mutant = args
        self.loggs[self.current_generation].append(
                f"{self.current_generation}: [{type(operator).__name__}]  " + 
                f"{individual} ---> {mutant}"
                )

    def __crossover_log(self, operator, *args):
        parent1, parent2, child1, child2, population = args
        self.loggs[self.current_generation].append(
                f"{self.current_generation}: [{type(operator).__name__}] " +
                f"{parent1} x {parent2}" +
                " ----> " +
                f"{child1} && {child2}"

                )
