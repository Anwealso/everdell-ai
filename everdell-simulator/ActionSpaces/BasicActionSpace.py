from abc import abstractmethod
from Worker import Worker
from Player import Player
from resources import ResourceValue
from Cards.Card import Card
from ActionSpaces.ActionSpace import ActionSpace


class BasicActionSpace(ActionSpace):

    def __init__(self, value: ResourceValue, numCardsDraw: int, isShared: bool) -> None:
        self.value: int = value
        self.numCardsDraw: int = numCardsDraw
        self.isShared: bool = isShared

        def useEffect(self, player: Player):
            player.giveCards(self.numCardsDraw)
            player.giveResources(self.value)

        super(useEffect)

    def hasAvailableSlot(self, player: Player) -> bool:
        """
        Checks whether the actionspace has an available slot
        """
        return len(self.workers) == 0 or self.isShared
