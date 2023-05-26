import sys
import math
from enum import Enum

DEBUG = True

def debug(msg):
    if DEBUG:
        print(msg, file=sys.stderr)


class CellType(Enum):
    OTHER = 0
    EGGS = 1
    CRYSTAL = 2

    def __int__(self):
        return self.value


class CellInfo:

    def __init__(self, idx, type, initial_resources, neighs):
        self.idx = idx  # Cell index
        self.type = CellType(type)  # Cell type
        self.resources = initial_resources  # Initial resources
        self.my_ants = 0  # Amount of your ants on this cell
        self.opp_ants = 0  # Amount of opponent ants on this cell
        self.neighs = neighs  # Neighbouring cells

    def __lt__(self, other):
        return self.resources < other.resources

    def update(self, resources, my_ants, opp_ants):
        self.resources = resources
        self.my_ants = my_ants
        self.opp_ants = opp_ants


class Map:
    def __init__(self):
        self.number_of_cells = int(input())  # amount of hexagonal cells in this map
        self.cells = []
        for i in range(self.number_of_cells):
            # _type: 0 for empty, 1 for eggs, 2 for crystal
            # initial_resources: the initial amount of eggs/crystals on this cell
            # neigh_0: the index of the neighbouring cell for each direction
            _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
            neighs = [neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5]
            self.cells.append(CellInfo(i, _type, initial_resources, neighs))

    def update_input_data(self):
        for i in range(self.number_of_cells):
            # resources: the current amount of eggs/crystals on this cell
            # my_ants: the amount of your ants on this cell
            # opp_ants: the amount of opponent ants on this cell
            resources, my_ants, opp_ants = [int(j) for j in input().split()]
            self.cells[i].update(resources, my_ants, opp_ants)

    def get_best_cells(self, origin, turn):
        output = ''
        strength = 10
        n_turns = 5
        aux_cells = self.cells.copy()
        aux_cells.sort(reverse=True)

        for c in aux_cells:
            # debug(f"idx:{c.idx} type:{c.type.value} - {c.resources}")
            if turn >= n_turns and c.type == CellType.CRYSTAL:
                output += f"LINE {origin} {c.idx} {strength};"
                strength -= 1
            elif turn < n_turns and c.type == CellType.EGGS:
                output += f"LINE {origin} {c.idx} {10};"
                break
        return output[:-1]


class CodingameSpring():
    def __init__(self):
        self.turn = 0
        self.map = Map()
        self.number_of_bases = int(input())

        for i in input().split():
            self.my_base_index = int(i)
        for i in input().split():
            self.opp_base_index = int(i)

        self.action = 'WAIT'

    def loop(self):
        while True:
            self.get_new_input_data()
            self.think()
            self.output()
            self.turn += 1

    def get_new_input_data(self):
        self.map.update_input_data()

    def think(self):
        self.action = self.map.get_best_cells(self.my_base_index, self.turn)

    def output(self):
        # Write an action using print
        print(self.action)


def main():
    game = CodingameSpring()
    game.loop()


if __name__ == "__main__":
    main()