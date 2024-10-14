from Player import Player
from resources import ResourceValue
from ActionSpaces.ActionSpace import ActionSpace


class ForestActionSpace(ActionSpace):

    def __init__(self, useEffect: function, maxWorkers: int) -> None:
        self.maxWorkers: int = maxWorkers
        super(useEffect)

    def hasAvailableSlot(self, player: Player) -> bool:
        """
        Checks whether the actionspace has an available slot for this specific player
        """
        return (
            player.name not in [worker.owner for worker in self.workers]
            and len(self.workers) < self.maxWorkers
        )

    def get_all() -> list[ForestActionSpace]:
        all_forest_cards: list[ForestActionSpace] = []

        # "Copy any Basic location and draw 1 card."
        # "2 berries & 1 card"
        # "Draw 2 meadow cards and play 1 for -1 any"
        # "Discard any, then draw 2 for every card discarded."
        all_forest_cards.append(
            ForestActionSpace(
                lambda player: player.giveResource(ResourceValue(0, 0, 0, 3)), 2
            )
        )  # "3 berries"
        all_forest_cards.append(
            ForestActionSpace(
                lambda player: player.giveResource(ResourceValue(1, 1, 0, 1)), 2
            )
        )  # "1 twig, 1 resin & 1 berry"
        # "Discard up to 3 cards & gain Lany for each card."
        all_forest_cards.append(
            ForestActionSpace(
                lambda player: player.giveResource(ResourceValue(1, 2, 0, 0)), 2
            )
        )  # "2 resin & 1 twig"
        # "2 cards & 1 any"
        # "3 cards & 1 pebble"
        # "2 any"


# create addNumbers static method
ForestActionSpace.all_forest_cards = staticmethod(ForestActionSpace.all_forest_cards)
