class Reader:
    def __init__(self, filename):
        self.filename = filename
        self.node_set = []


    def read_data(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()

            node_set_line = lines[0].strip()
            nodes = node_set_line.split(',')
            for node in nodes:
                coords = node.split()
                if 1 < float(coords[0]) < 30 and 1 < float(coords[1]) < 30:
                    self.node_set.append((float(coords[0]), float(coords[1])))
        return self.node_set
