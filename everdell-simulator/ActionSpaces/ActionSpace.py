from abc import abstractmethod
from Worker import Worker
from Player import Player
from resources import ResourceValue
from Cards.Card import Card


class ActionSpace:

    def __init__(self, useEffect: function) -> None:
        self.workers: list[Worker] = []
        # The effect that is triggered when the space is visited.
        # This effect could be gaining resources, or drawing or discarding cards with various condition
        self.useEffect: function = useEffect
        pass

    @abstractmethod
    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot for the player
        """
        pass

    def getWorkers(self):
        return self.workers

    def addWorker(self, worker: Worker):
        """
        Adds a worker to the actionspace
        """
        if self.hasAvailableSlot():
            self.workers.append(worker)
        else:
            raise Exception("No slots available to add worker to.")

    def removeAllWorkers(self):
        """
        Removes all the workers from the aciton space
        """
        self.workers.clear()


class BasicActionSpace(ActionSpace):

    def __init__(self, value: ResourceValue, numCardsDraw: int, isShared: bool) -> None:
        self.value: int = value
        self.numCardsDraw: int = numCardsDraw
        self.isShared: bool = isShared

        def useEffect(self, player: Player):
            player.giveCards(self.numCardsDraw)
            player.giveResources(self.value)

        super(useEffect)

    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot
        """
        return len(self.workers) == 0 or self.isShared


class ForestActionSpace(ActionSpace):

    def __init__(self, useEffect: function, maxWorkers: int) -> None:
        self.maxWorkers: int = maxWorkers
        super(useEffect)

    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot for this specific player
        """
        return (
            player.name not in [worker.owner for worker in self.workers]
            and len(self.workers) < self.maxWorkers
        )


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
