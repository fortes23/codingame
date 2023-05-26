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

    def __init__(self, idx, type, initial_resources):
        self.idx = idx  # Cell index
        self.type = CellType(type)  # Cell type
        self.resources = initial_resources  # Initial resources

    def update(self, resources):
        self.resources = resources
        # debug(f"Cell[{self.idx}] type[{self.type.value}] resources[{self.resources}]")


number_of_cells = int(input())  # amount of hexagonal cells in this map

cells = []

for i in range(number_of_cells):
    # _type: 0 for empty, 1 for eggs, 2 for crystal
    # initial_resources: the initial amount of eggs/crystals on this cell
    # neigh_0: the index of the neighbouring cell for each direction
    _type, initial_resources, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
    # debug(f"i[{i}] type[{_type}] initial_resources [{initial_resources}] neigh_0[{neigh_0}] neigh_1[{neigh_1}] neigh_2[{neigh_2}] neigh_3[{neigh_3}] neigh_4[{neigh_4}] neigh_5[{neigh_5}]")
    cells.append(CellInfo(i, _type, initial_resources))

number_of_bases = int(input())
for i in input().split():
    my_base_index = int(i)
    # debug(f"i[{i}] my_base_index[{my_base_index}]")
for i in input().split():
    opp_base_index = int(i)
    # debug(f"i[{i}] opp_base_index[{opp_base_index}]")

# game loop
while True:
    idx = -1
    output = ''
    res_cells = []
    for i in range(number_of_cells):
        # resources: the current amount of eggs/crystals on this cell
        # my_ants: the amount of your ants on this cell
        # opp_ants: the amount of opponent ants on this cell
        resources, my_ants, opp_ants = [int(j) for j in input().split()]
        cells[i].update(resources)
        if cells[i].type == CellType.CRYSTAL:
            res_cells.append((i, resources))
        else:
            res_cells.append((i, 0))

    sorted(res_cells, key=lambda x: x[1])
    strength = 10
    for r in res_cells:
        if r[1]:
            output += f"LINE {my_base_index} {r[0]} {strength};"
            strength -= 1
    # print(f"LINE {my_base_index} {idx} 5")
    print(f"{output[:len(output)-1]}")

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # WAIT | LINE <sourceIdx> <targetIdx> <strength> | BEACON <cellIdx> <strength> | MESSAGE <text>
    # print("WAIT")
