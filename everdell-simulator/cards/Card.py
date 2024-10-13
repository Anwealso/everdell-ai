"""
card.py
Alex Nicholson
12/08/2024

An everdell card (this is the superclass that all cards descend from)

In everdell playing a card can take allow you to draw resources from the pots,
draw card(s), take cards from other players or be awarded points.
"""

from abc import abstractmethod
from enum import Enum
from resources import ResourceValue
from Player import Player


class Card:

    def __init__(
        self,
        name: str,
        cost: ResourceValue,
        score_value: int,
        unique: bool,
        use_effect: function,
    ):
        self.name: str = name
        self.cost: ResourceValue = cost
        self.score_value: int = score_value
        self.unique = unique
        self.triggered: bool = (
            False  # do we need this or do cards just trigger instantaneously on playing / placing critter on
        )
        self.use_effect: function = use_effect


class CritterCard(Card):

    def __init__(
        self,
        name: str,
        cost: ResourceValue,
        score_value: int,
        unique: bool,
        use_effect: function,
    ):
        super(name, cost, score_value, unique, use_effect)


class ConstructionCard(Card):

    def __init__(
        self,
        name: str,
        cost: ResourceValue,
        score_value: int,
        unique: bool,
        use_effect: function,
    ):
        super(name, cost, score_value, unique, use_effect)
        self.occupied = False


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
