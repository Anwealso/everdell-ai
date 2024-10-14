from Player import Player
from resources import ResourceValue
from Cards.Card import Card
from ActionSpaces.ActionSpace import ActionSpace


class Haven(ActionSpace):

    def __init__(self, useEffect: function) -> None:
        self.isShared: bool = True

        def useEffect(
            self,
            player: Player,
            cards: list[Card],
            discard_pile: list[Card],
            resources: ResourceValue,
        ):
            """
            Player discards any number of cards from their hand,
            and gain 1 of any resource for every 2 cards discarded.
            """
            if resources.sum() != len(cards // 2):
                Player.takeCards(cards)
                discard_pile.append(cards)
                Player.giveResources(resources)
            else:
                raise Exception(
                    "Incorrect number of resources requested (resources requested must be equal to floor(numCards/2))."
                )
            pass

        super(useEffect)

    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot
        """
        return len(self.workers) == 0 or self.isShared
