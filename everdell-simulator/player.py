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
from Worker import Worker


class Player:
    def __init__(self, name):
        """
        Inits the everdell player class
        """
        self.name = name
        self.resources: ResourceValue = ResourceValue(0, 0, 0, 0)
        self.workers: list[Worker] = [  # start with 4 workers
            Worker(self.name),
            Worker(self.name),
            Worker(self.name),
            Worker(self.name),
        ]
        self.points = 0
        self.hand = []  # the players hand of cards

    def getInput(self, strategy="random"):
        """
        Returns the player action
        """

        if strategy == "random":
            return random.choice(utils.Action)

    def getAction(self, interactive="true"):
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

    def giveCard(self, card):
        """
        Removes a card from the players hand

        Args:
            - card [Card]: the card to add
        """
        self.hand.append(card)

    def takeCard(self, card):
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

    def giveResources(self, value: ResourceValue):
        self.resources += value

    def takeResources(self, value: ResourceValue):
        self.resources -= value
