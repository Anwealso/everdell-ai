from Card import Card
from Player import Player
from resources import ResourceValue


class Farm(Card):
    def __init__(self, category, name, cost, scoreValue):
        super(category, name, cost, scoreValue)
        pass

    def use_effect(self, user: Player):
        """
        "gain 1b"
        """
        if not self.triggered:
            Player.resources += ResourceValue(0, 0, 0, 1)
        else:
            raise Exception("Card has already been triggered.")
