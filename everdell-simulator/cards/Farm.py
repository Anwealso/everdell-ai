from Card import Card
from Player import Player
from resources import ResourceValue


class Farm(Card):
    def __init__(self, category, name, cost, score_value):
        def use_effect(self, user: Player):
            """
            "gain 1b"
            """
            if not self.triggered:
                Player.resources += ResourceValue(0, 0, 0, 1)
            else:
                raise Exception("Card has already been triggered.")

        super(category, name, cost, score_value, use_effect)
        pass
