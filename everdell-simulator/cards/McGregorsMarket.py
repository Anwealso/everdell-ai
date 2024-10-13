from Card import Card
from Player import Player
from resources import ResourceValue, ResourceType


class McGregorsMarket(Card):
    def __init__(self, category, name, cost, score_value):
        def use_effect(self, user: Player, resource_type: ResourceType):
            """
            "gain 2a"
            """
            resourceValue = ResourceValue(
                2 if resource_type == ResourceType.TWIG else 0,
                2 if resource_type == ResourceType.RESIN else 0,
                2 if resource_type == ResourceType.PEBBLE else 0,
                2 if resource_type == ResourceType.BERRY else 0,
            )

            if not self.triggered:
                Player.resources += resourceValue
            else:
                raise Exception("Card has already been triggered.")

        super(category, name, cost, score_value, use_effect)
        pass
