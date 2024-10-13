from Card import Card
from Player import Player
from Card import CardCategory
from ActionSpaces.ActionSpace import CardActionSpace
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
        on_play: function,
        isOpen: bool,
        on_add_worker: function,
    ) -> None:
        super(category, name, cost, score_value, on_play)
        self.isOpen: bool = isOpen
        self.action_space = CardActionSpace(on_add_worker, isOpen)
        pass
