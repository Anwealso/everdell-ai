from Worker import Worker


class ActionSpace:

    def __init__(self, value, numWorkerSlots) -> None:
        self.value: int = value
        self.availableSlots: int = numWorkerSlots
        self.workers: list[Worker] = []
        pass

    def hasAvailableSlot(self):
        return self.availableSlots > 0

    def getWorkers(self):
        return self.workers

    def addWorker(self, worker: Worker):
        if self.hasAvailableSlot():
            self.workers.append(worker)
        else:
            raise Exception("No slots available to add worker to.")
