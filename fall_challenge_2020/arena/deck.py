from spell import TomeSpell, DeliverySpell
from inventory import Inventory

class Deck():
    def __init__(self):
        self.tome = []
        self.deliveries = []

        self.tome.append(TomeSpell(Inventory(-3, 0, 0, 1)))
        self.tome.append(TomeSpell(Inventory(3, -1, 0, 0)))
        self.tome.append(TomeSpell(Inventory(1, 1, 0, 0)))
        self.tome.append(TomeSpell(Inventory(0, 0, 1, 0)))
        self.tome.append(TomeSpell(Inventory(3, 0, 0, 0)))
        self.tome.append(TomeSpell(Inventory(2, 3, -2, 0)))
        self.tome.append(TomeSpell(Inventory(2, 1, -2, 1)))
        self.tome.append(TomeSpell(Inventory(3, 0, 1, -1)))
        self.tome.append(TomeSpell(Inventory(3, -2, 1, 0)))
        self.tome.append(TomeSpell(Inventory(2, -3, 2, 0)))
        self.tome.append(TomeSpell(Inventory(2, 2, 0, -1)))
        self.tome.append(TomeSpell(Inventory(-4, 0, 2, 0)))
        self.tome.append(TomeSpell(Inventory(2, 1, 0, 0)))
        self.tome.append(TomeSpell(Inventory(4, 0, 0, 0)))
        self.tome.append(TomeSpell(Inventory(0, 0, 0, 1)))
        self.tome.append(TomeSpell(Inventory(0, 2, 0, 0)))
        self.tome.append(TomeSpell(Inventory(1, 0, 1, 0)))
        self.tome.append(TomeSpell(Inventory(-2, 0, 1, 0)))
        self.tome.append(TomeSpell(Inventory(-1, -1, 0, 1)))
        self.tome.append(TomeSpell(Inventory(0, 2, -1, 0)))
        self.tome.append(TomeSpell(Inventory(2, -2, 0, 1)))
        self.tome.append(TomeSpell(Inventory(-3, 1, 1, 0)))
        self.tome.append(TomeSpell(Inventory(0, 2, -2, 1)))
        self.tome.append(TomeSpell(Inventory(1, -3, 1, 1)))
        self.tome.append(TomeSpell(Inventory(0, 3, 0, -1)))
        self.tome.append(TomeSpell(Inventory(0, -3, 0, 2)))
        self.tome.append(TomeSpell(Inventory(1, 1, 1, -1)))
        self.tome.append(TomeSpell(Inventory(1, 2, -1, 0)))
        self.tome.append(TomeSpell(Inventory(4, 1, -1, 0)))
        self.tome.append(TomeSpell(Inventory(-5, 0, 0, 2)))
        self.tome.append(TomeSpell(Inventory(-4, 0, 1, 1)))
        self.tome.append(TomeSpell(Inventory(0, 3, 2, -2)))
        self.tome.append(TomeSpell(Inventory(1, 1, 3, -2)))
        self.tome.append(TomeSpell(Inventory(-5, 0, 3, 0)))
        self.tome.append(TomeSpell(Inventory(-2, 0, -1, 2)))
        self.tome.append(TomeSpell(Inventory(0, 0, -3, 3)))
        self.tome.append(TomeSpell(Inventory(0, -3, 3, 0)))
        self.tome.append(TomeSpell(Inventory(-3, 3, 0, 0)))
        self.tome.append(TomeSpell(Inventory(-2, 2, 0, 0)))
        self.tome.append(TomeSpell(Inventory(0, 0, -2, 2)))
        self.tome.append(TomeSpell(Inventory(0, -2, 2, 0)))
        self.tome.append(TomeSpell(Inventory(0, 0, 2, -1)))

        self.deliveries.append(DeliverySpell(Inventory(2, 2, 0, 0), 6))
        self.deliveries.append(DeliverySpell(Inventory(3, 2, 0, 0), 7))
        self.deliveries.append(DeliverySpell(Inventory(0, 4, 0, 0), 8))
        self.deliveries.append(DeliverySpell(Inventory(2, 0, 2, 0), 8))
        self.deliveries.append(DeliverySpell(Inventory(2, 3, 0, 0), 8))
        self.deliveries.append(DeliverySpell(Inventory(3, 0, 2, 0), 9))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 2, 0), 10))
        self.deliveries.append(DeliverySpell(Inventory(0, 5, 0, 0), 10))
        self.deliveries.append(DeliverySpell(Inventory(2, 0, 0, 2), 10))
        self.deliveries.append(DeliverySpell(Inventory(2, 0, 3, 0), 11))
        self.deliveries.append(DeliverySpell(Inventory(3, 0, 0, 2), 11))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 4, 0), 12))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 0, 2), 12))
        self.deliveries.append(DeliverySpell(Inventory(0, 3, 2, 0), 12))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 3, 0), 13))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 2, 2), 14))
        self.deliveries.append(DeliverySpell(Inventory(0, 3, 0, 2), 14))
        self.deliveries.append(DeliverySpell(Inventory(2, 0, 0, 3), 14))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 5, 0), 15))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 0, 4), 16))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 0, 3), 16))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 3, 2), 17))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 2, 3), 18))
        self.deliveries.append(DeliverySpell(Inventory(0, 0, 0, 5), 20))
        self.deliveries.append(DeliverySpell(Inventory(2, 1, 0, 1), 9))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 1, 1), 12))
        self.deliveries.append(DeliverySpell(Inventory(1, 0, 2, 1), 12))
        self.deliveries.append(DeliverySpell(Inventory(2, 2, 2, 0), 13))
        self.deliveries.append(DeliverySpell(Inventory(2, 2, 0, 2), 15))
        self.deliveries.append(DeliverySpell(Inventory(2, 0, 2, 2), 17))
        self.deliveries.append(DeliverySpell(Inventory(0, 2, 2, 2), 19))
        self.deliveries.append(DeliverySpell(Inventory(1, 1, 1, 1), 12))
        self.deliveries.append(DeliverySpell(Inventory(3, 1, 1, 1), 14))
        self.deliveries.append(DeliverySpell(Inventory(1, 3, 1, 1), 16))
        self.deliveries.append(DeliverySpell(Inventory(1, 1, 3, 1), 18))
        self.deliveries.append(DeliverySpell(Inventory(1, 1, 1, 3), 20))