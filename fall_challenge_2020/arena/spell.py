from inventory import Inventory


class Spell():
    INSTANCE_COUNT = 0

    def __init__(self, inventory, score=0, stock=0, repeatable=True, active=False):
        self.id = Spell.INSTANCE_COUNT
        self.active = active
        self.repeatable = repeatable
        self.inventory = inventory
        self.score = score
        self.stock = stock
        Spell.INSTANCE_COUNT += 1


class TomeSpell(Spell):
    def __init__(self, recipe):
        super().__init__(recipe, repeatable=any(z == 0 for z in recipe.deltas))


class DeliverySpell(Spell):
    def __init__(self, need, score):
        super().__init__(Inventory(-need.deltas[0], -need.deltas[1], -need.deltas[2], -need.deltas[3]), score=score, repeatable=False)
