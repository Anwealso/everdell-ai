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


class CardCategory(Enum):
    CONSTRUCTION = 1
    CREATURE = 2


class Card:
    def __init__(self, category, name, cost, scoreValue):
        self.category: CardCategory = category
        self.name: str = name
        self.cost: ResourceValue = cost
        self.scoreValue: int = scoreValue
        self.triggered: bool = False
        pass

    @abstractmethod
    def use_effect(self, user: Player):
        """
        Executes the action of the card
        """
        pass
