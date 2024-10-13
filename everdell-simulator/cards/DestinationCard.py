from Card import Card
from Player import Player
from Card import CardCategory
from Worker import Worker
from ActionSpaces.ActionSpace import CardActionSpace
from resources import ResourceValue


class DestinationCard(Card):
    """
    A destination card also has an ActionSpace on it where a worker can be placed (can be your's or an opponent's worker).
    """

    def __init__(
        self,
        name: str,
        cost: ResourceValue,
        score_value: int,
        on_play: function,
        isOpen: bool,
        on_add_worker: function,
    ) -> None:
        super(CardCategory.CONSTRUCTION, name, cost, score_value, on_play)
        self.isOpen: bool = isOpen
        self.action_space = CardActionSpace(on_add_worker, isOpen)
        pass

    def hasAvailableSlot(self, player: Player) -> bool:
        """
        Checks whether the card's actionspace has an available slot for this specific player
        """
        return self.action_space.hasAvailableSlot(player)

    def getWorkers(self) -> list[Worker]:
        """
        Checks whether the card's actionspace has an available slot for this specific player
        """
        return self.action_space.getWorkers()

    def addWorker(self, worker: Worker) -> None:
        """
        Adds a worker to the card's actionspace
        """
        return self.action_space.addWorker(worker)

    def removeAllWorkers(self) -> None:
        """
        Removes all the workers from the card's action space
        """
        return self.action_space.removeAllWorkers()
