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
    CRITTER = 2


class Card:
    def __init__(
        self,
        category: CardCategory,
        name: str,
        cost: ResourceValue,
        score_value: int,
        use_effect: function,
    ):
        self.category: CardCategory = category
        self.name: str = name
        self.cost: ResourceValue = cost
        self.score_value: int = score_value
        self.triggered: bool = False
        self.triggered: function = use_effect
        pass
