import subprocess
import random

from inventory import Inventory
from deck import Deck
from player import Player
from spelltype import SpellType

INGREDIENT_TYPE = 4
COUNTER_SIZE = 5
TOME_SIZE = 6
MAX_ROUNDS = 100
DELIVERY_GOAL = 6

class Game():

    def __init__(self, bot1, bot2, debug=False):
        self.debug = debug

        self.round = 0
        self.deck = Deck()
        self.bonus = [4, 4]

        random.shuffle(self.deck.tome)
        random.shuffle(self.deck.deliveries)

        self.deliveries = self.deck.deliveries[:COUNTER_SIZE]
        self.deck.deliveries = self.deck.deliveries[COUNTER_SIZE:]

        self.tome = self.deck.tome[:TOME_SIZE]
        self.tomestockgain = [0] * TOME_SIZE
        self.deck.tome = self.deck.tome[TOME_SIZE:]

        proc1 = subprocess.Popen(bot1,
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        proc2 = subprocess.Popen(bot2,
                                 stdout=subprocess.PIPE, stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE)

        self.player1 = Player(proc1)
        self.player2 = Player(proc2)

    def get_bonus_value(self, spell):
        return 1
        pass

    def get_number_bonus(self, spell):
        return 0
        pass

    def generate_msg(self, player, other_player):
        # Amount
        msg = [len(self.deliveries) + len(self.tome) + len(player.spells) + len(other_player.spells)]

        # Deliveries
        for d in self.deliveries:
            msg.append("{} {} {} {} {} {} {} {}".format(
                       d.id, SpellType.BREW.name, d.inventory.to_string(), d.score, self.get_bonus_value(d), 
                       self.get_number_bonus(d), int(d.active), int(d.repeatable)))

        # Spells and tomes
        for t in self.tome:
            msg.append("{} {} {} {} {} {} {} {}".format(
                       t.id, SpellType.LEARN.name, t.inventory.to_string(), t.score,
                       self.tome.index(t), t.stock, int(t.active), int(t.repeatable)))

        for s in player.spells:
            msg.append("{} {} {} {} {} {} {} {}".format(
                       s.id, SpellType.CAST.name, s.inventory.to_string(), s.score,
                       player.spells.index(s), s.stock, int(s.active), int(s.repeatable)))

        for s in other_player.spells:
            msg.append("{} {} {} {} {} {} {} {}".format(
                       s.id, SpellType.OPPONENT_CAST.name, s.inventory.to_string(), s.score,
                       other_player.spells.index(s), s.stock, int(s.active), int(s.repeatable)))

        # Inventory and scores
        msg.append("{} {}".format(player.inventory.to_string(), player.score))
        msg.append("{} {}".format(other_player.inventory.to_string(), other_player.score))
        return msg

    def match(self):
        while self.round < MAX_ROUNDS:
            return
