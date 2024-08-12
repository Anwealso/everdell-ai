"""
card.py
Alex Nicholson
12/08/2024

Various utility classes, functions, and constants for use in the everdell game
"""

from enum import Enum


class Action(Enum):
    DRAW_CARD = "D"
    PLAY_CARD = "P"


class Resource(Enum):
    BERRY = 1
    TWIG = 2
    RESIN = 3
    PEBBLE = 4


def string_to_action(input_string):
    for action in Action:
        if input_string == action.value:
            return action
    return None
