class Inventory():
    def __init__(self, a=0, b=0, c=0, d=0):
        self.deltas = [a, b, c, d]

    def __add__(self, other):
        aux = [self.deltas[i] + other.deltas[i] for i in range(len(self.deltas))]
        return Inventory(aux[0], aux[1], aux[2], aux[3])

    def __iter__(self):
        yield self.deltas[0]
        yield self.deltas[1]
        yield self.deltas[2]
        yield self.deltas[3]

    def to_string(self):
        aux = ""
        for d in self.deltas:
            aux += str(d) + " "

        return aux[:-1]
