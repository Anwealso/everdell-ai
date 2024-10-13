from abc import abstractmethod
from Worker import Worker
from Player import Player
from resources import ResourceValue


class ActionSpace:

    def __init__(self, value: ResourceValue, numCardsDraw: int) -> None:
        self.value: int = value
        self.numCardsDraw: int = numCardsDraw
        self.workers: list[Worker] = []
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
        super(value, numCardsDraw)
        self.isShared: bool = isShared

    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot
        """
        return len(self.workers) == 0 or self.isShared


class ForestActionSpace(ActionSpace):

    def __init__(
        self, value: ResourceValue, numCardsDraw: int, maxWorkers: int
    ) -> None:
        super(value, numCardsDraw)
        self.maxWorkers: int = maxWorkers

    def hasAvailableSlot(self, player: Player):
        """
        Checks whether the actionspace has an available slot for this specific player
        """
        return (
            player.name not in [worker.owner for worker in self.workers]
            and len(self.workers) < self.maxWorkers
        )
