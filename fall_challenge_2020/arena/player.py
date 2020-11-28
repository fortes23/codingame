from inventory import Inventory
from spell import Spell


class Player():
    def __init__(self, proc, inventory=Inventory(3,0,0,0), init_score=0):
        self.inventory = inventory
        self.spells = self.init_spells()
        self.score = init_score
        self.proc = proc
        self.ndeliveries = 0

    def __del__(self):
        self.proc.kill()

    def init_spells(self):
        return [Spell(Inventory(2, 0, 0, 0)),
                Spell(Inventory(-1, 1, 0, 0)),
                Spell(Inventory(0, -1, 1, 0)),
                Spell(Inventory(0, 0, -1, 1))]
