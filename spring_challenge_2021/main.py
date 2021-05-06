import sys
from enum import Enum
import collections


def debug(msg):
    print(msg, file=sys.stderr)

class RichnessType(Enum):
    UN_Q  = 0
    LOW_Q = 1
    MED_Q = 2
    HIG_Q = 3

class ActionType(Enum):
    COMPLETE = 1
    WAIT = 2
    GROW = 3
    SEED = 4

    @staticmethod
    def action_to_string(action):
        return action.name

    @staticmethod
    def string_to_action(_string):
        for a in ActionType:
            if a.name == _string:
                return a

class Tree():
    def __init__(self, index, size, mine, dormant):
        self.cell_index = index
        self.size = size
        self.mine = mine
        self.dormant = dormant

    @staticmethod
    def read_next_tree():
        inputs = input().split()
        return Tree(int(inputs[0]), int(inputs[1]), inputs[2] != "0", inputs[3] != "0")

class Forest():
    def __init__(self):
        self.n_cells = int(input())
        self.for_map = {}
        for _ in range(self.n_cells):
            index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]
            self.for_map.update({index: {"richness": richness, "tree": None}})
        self.n_trees = 0

    def read_next_trees(self, num_trees):
        for _ in range(0, num_trees):
            new_tree = Tree.read_next_tree()
            self.for_map[new_tree.cell_index]["tree"] = new_tree

    def get_points(self, cell_index):
        points = (self.for_map[cell_index]["richness"] - 1) * 2 + 1
        return points

class Action():
    def __init__(self, action_val, cur_forest=None):
        act = action_val.split()
        self.action_type = ActionType.string_to_action(act[0])
        self.points = 0
        self.cell_index = ""
        if len(act) > 1:
            self.cell_index = int(act[1])
            self.points = cur_forest.get_points(self.cell_index)

    def output(self):
        print(ActionType.action_to_string(self.action_type) + " " + str(self.cell_index))

    @staticmethod
    def read_next_action(cur_forest):
        action_type = input()
        return Action(action_type, cur_forest)

    @staticmethod
    def read_next_actions(num_action, cur_forest):
        result = []
        for _ in range(0, num_action):
            result.append(Action.read_next_action(cur_forest))
        return result

class WoodSpirit():
    def __init__(self):
        self.sun = 0
        self.score = 0
        self.waiting = False
        self.nutrients = 0
        self.next_action = None

    def read_next_spirit_info(self, opponent=False):
        if not opponent:
            self.nutrients = int(input())
            self.sun, self.score = [int(i) for i in input().split()]
        else:
            inputs = input().split()
            self.sun = int(inputs[0])
            self.score = int(inputs[1])
            self.waiting = inputs[2] != "0"

def get_best_action(lst_actions):
    best = lst_actions[0]
    for act in lst_actions:
        if act.points > best.points:
            best = act
    return best

class CodingameSpring():
    def __init__(self):
        self.day = 0
        self.forest = Forest()
        self.my_spirit = WoodSpirit()
        self.oponent_spirit= WoodSpirit()
        self.actions = []

    def loop(self):
        while True:
            self.get_new_input_data()
            self.think()
            self.output()

    def get_new_input_data(self):
        self.day = int(input())
        self.actions.clear()
        self.my_spirit.next_action = None
        self.my_spirit.read_next_spirit_info()
        self.oponent_spirit.read_next_spirit_info(opponent=True)
        number_of_trees = int(input())
        self.forest.read_next_trees(number_of_trees)
        action_count = int(input())
        self.actions = Action.read_next_actions(action_count, self.forest)

    def think(self):
        if self.my_spirit.nutrients == 0:
            return

        self.my_spirit.next_action = get_best_action(self.actions)

    def output(self):
        # Write an action using print
        if self.my_spirit.next_action:
            self.my_spirit.next_action.output()
        else:
            print("WAIT")


def main():
    game = CodingameSpring()
    game.loop()


if __name__ == "__main__":
    main()
