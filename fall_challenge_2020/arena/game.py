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
        self.bonus_value = [3, 1]

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
        if self.get_bonus_amount(spell) == 0:
            return 0

        index = self.deliveries.index(spell)

        if index < 0 or index > 1:
            return 0

        return self.bonus_value[index]

    def get_bonus_amount(self, spell):
        index = self.deliveries.index(spell)

        if index < 0 or index > 1:
            return 0

        return self.bonus[index]

    def generate_msg(self, player, other_player):
        # Amount
        msg = [len(self.deliveries) + len(self.tome) + len(player.spells) + len(other_player.spells)]

        # Deliveries
        for d in self.deliveries:
            msg.append("{action_id} {action_type} {deltas} {price} {tome_index} {tax_count} {castable} {repeatable}".format(
                       action_id=d.id, action_type=SpellType.BREW.name, deltas=d.inventory.to_string(), price=d.score,
                       tome_index=self.get_bonus_value(d), tax_count=self.get_bonus_amount(d), castable=int(d.active),
                       repeatable=int(d.repeatable)))

        # Spells and tomes
        for t in self.tome:
            msg.append("{action_id} {action_type} {deltas} {price} {tome_index} {tax_count} {castable} {repeatable}".format(
                       action_id=t.id, action_type=SpellType.LEARN.name, deltas=t.inventory.to_string(), price=t.score,
                       tome_index=self.tome.index(t), tax_count=t.stock, castable=int(t.active), repeatable=int(t.repeatable)))

        for s in player.spells:
            msg.append("{action_id} {action_type} {deltas} {price} {tome_index} {tax_count} {castable} {repeatable}".format(
                       action_id=s.id, action_type=SpellType.CAST.name, deltas=s.inventory.to_string(), price=s.score,
                       tome_index=player.spells.index(s), tax_count=s.stock, castable=int(s.active), repeatable=int(s.repeatable)))

        for s in other_player.spells:
            msg.append("{action_id} {action_type} {deltas} {price} {tome_index} {tax_count} {castable} {repeatable}".format(
                       action_id=s.id, action_type=SpellType.OPPONENT_CAST.name, deltas=s.inventory.to_string(), price=s.score,
                       tome_index=other_player.spells.index(s), tax_count=s.stock, castable=int(s.active), repeatable=int(s.repeatable)))

        # Inventory and scores
        msg.append("{} {}".format(player.inventory.to_string(), player.score))
        msg.append("{} {}".format(other_player.inventory.to_string(), other_player.score))
        return msg

    def match(self):
        while self.round < MAX_ROUNDS:
            return
