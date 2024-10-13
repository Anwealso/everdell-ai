from Card import Card
from Player import Player
from Card import CardCategory
from ActionSpaces.ActionSpace import ActionSpace
from resources import ResourceValue


class DestinationCard(Card):
    """
    A destination card also has an ActionSpace on it where a worker can be placed (can be your's or an opponent's worker).
    """

    def __init__(
        self,
        category: CardCategory,
        name: str,
        cost: ResourceValue,
        score_value: int,
        action_space: ActionSpace,
        use_effect: function,
    ):
        super(category, name, cost, score_value, use_effect)
        self.action_space = action_space
        pass
