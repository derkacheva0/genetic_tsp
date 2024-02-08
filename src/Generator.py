import random
class Generator:
    def __init__(self):
        self.filename = 'txt-files/gen.txt'
        self.n = 5
        self.node_set = []

    def generate_data(self):
        for _ in range(self.n):
            x = round(random.uniform(1, 30), 1)
            y = round(random.uniform(1, 30), 1)
            self.node_set.append((x, y))
        return self.node_set

#это можно не сохранять, а проcто дaнные читать
    def save_data(self):
        with open(self.filename, 'w') as file:
            node_set_line = ', '.join([' '.join(str(coord) for coord in node) for node in self.node_set])
            file.write(node_set_line + '\n')
