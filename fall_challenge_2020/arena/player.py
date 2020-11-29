import os

from inventory import Inventory
from spell import Spell


class Player():
    def __init__(self, proc, inventory=Inventory(3,0,0,0), init_score=0, debug=False):
        self.inventory = inventory
        self.spells = self.init_spells()
        self.score = init_score
        self.proc = proc
        self.ndeliveries = 0
        self.debug = debug

    def __del__(self):
        self.proc.kill()

    def init_spells(self):
        return [Spell(Inventory(2, 0, 0, 0)),
                Spell(Inventory(-1, 1, 0, 0)),
                Spell(Inventory(0, -1, 1, 0)),
                Spell(Inventory(0, 0, -1, 1))]

    def send_input_line(self, msg):
        msg += "\n"
        os.write(self.proc.stdin.fileno(), msg.encode())

        if self.debug:
            print(os.read(self.proc.stderr.fileno(), 4096).decode('utf-8'))
