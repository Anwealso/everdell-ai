"""
player.py
Alex Nicholson
11/08/2024

An everdell game player - handles the cards and resources held by player as 
well as accepting player input and tracking player score.
"""

import utils
from random import random
from utils import Resource
from resources import ResourceValue


class Player:
    def __init__(self, name):
        """
        Inits the everdell player class
        """
        self.name = name
        self.resources: ResourceValue = 0
        self.points = 0
        self.hand = []  # the players hand of cards

    def get_input(self, strategy="random"):
        """
        Returns the player action
        """

        if strategy == "random":
            return random.choice(utils.Action)

    def get_action(self, interactive="true"):
        """
        Returns the player action
        """
        if interactive:
            while True:
                # Get the players input from STDIN
                playerInput = input(f"Enter action for player '{self.name}': ")
                action = utils.string_to_action(playerInput)
                if action is not None:
                    return action
                playerInput = input(f"Invalid input. Please enter a valid move")
        else:
            pass

    def add_card(self, card):
        """
        Removes a card from the players hand

        Args:
            - card [Card]: the card to add
        """
        self.hand.append(card)

    def remove_card(self, card):
        """
        Removes a card from the players hand

        Args:
            - card [Card]: the card to remove
        """
        if card not in self.hand:
            return Exception(
                f"Card {card} could not be removed as it does not currently exist in player {self.name}'s hand"
            )
        self.hand.remove(card)
