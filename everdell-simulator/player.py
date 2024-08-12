"""
player.py
Alex Nicholson
11/08/2024

An everdell game player - handles the cards and resources held by player as 
well as accepting player input and tracking player score.
"""

import random

import utils
from utils import Resource


class Player:
    def __init__(name=str(random.randint(1, 1000))):
        """
        Inits the everdell player class
        """
        self.name = name
        self.numBerry = 0
        self.numTwig = 0
        self.numBerry = 0
        self.numPebble = 0
        self.points = 0
        self.hand = []  # the players hand of cards

    def getInput(strategy="random"):
        """
        Returns the player action
        """

        if strategy == "random":
            return random.choice(utils.Action)

    def getAction(interactive="true"):
        """
        Returns the player action
        """
        if interactive:
            while True:
                # Get the players input from STDIN
                playerInput = input(f"Enter action for player '{self.name}': ")
                action = utils.stringToAction(playerInput)
                if action is not None:
                    break
        else:
            pass

    def addCard(card):
        """
        Removes a card from the players hand

        Args:
            - card [Card]: the card to add
        """
        self.hand.append(card)

    def removeCard(card):
        """
        Removes a card from the players hand

        Args:
            - card [Card]: the card to remove
        """
        if card not in self.hand.remove:
            return Exception(
                f"Card {card} could not be removed as it does not currently exist in player {self.name}'s hand"
            )
        self.hand.remove(card)

    def addResource(resource, qty):
        """
        Removes a card from the players hand

        Args:
            - resource [string]: the type of resource to add
            - qty [int]: the quantity of the resource to add
        """
        if resource == Resource.Berry:
            self.numBerry += qty
        elif resource == Resource.Twig:
            self.numTwig += qty
        elif resource == Resource.Resin:
            self.numBerry += qty
        elif resource == Resource.Pebble:
            self.numPebble += qty

    def removeResource(resource, qty):
        """
        Removes a card from the players hand

        Args:
            - resource [string]: the type of resource to remove
            - qty [int]: the quantity of the resource to remove
        """
        if resource == Resource.Berry:
            if self.numBerry < qty:
                return Exception(
                    f"Could not remove {qty}x {resource} from player (player only has {qty}x {resource})"
                )
            self.numBerry -= qty
        elif resource == Resource.Twig:
            if self.numTwig < qty:
                return Exception(
                    f"Could not remove {qty}x {resource} from player (player only has {qty}x {resource})"
                )
            self.numTwig -= qty
        elif resource == Resource.Resin:
            if self.numBerry < qty:
                return Exception(
                    f"Could not remove {qty}x {resource} from player (player only has {qty}x {resource})"
                )
            self.numBerry -= qty
        elif resource == Resource.Pebble:
            if self.numPebble < qty:
                return Exception(
                    f"Could not remove {qty}x {resource} from player (player only has {qty}x {resource})"
                )
            self.numPebble -= qty
