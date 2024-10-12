from Card import Card
from Player import Player


class Carnival(Card):
    def __init__(self, category, name, cost, scoreValue):
        super(category, name, cost, scoreValue)
        pass

    def use_effect(self, user: Player):
        """
        "draw 1 / green or gain 1a / 2 green"
        """
        pass
