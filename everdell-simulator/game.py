"""
game.py
Alex Nicholson
11/08/2024

This is the everdell game that holds all of the game state and input actions 
and state transitions.
"""

import utils
from player import *


class Game:
    def __init__(num_players):
        """
        Inits the everdell game class

        Args:
            - All of the game args
        """
        self.players = [Player() for player in num_players]

    def step():
        """
        Step the game state
        """
        self.handlePlayerInput()

    def getPlayerInput(player):
        """
        Get player input from the player and handle the transfre of cards and
        resources to/from the discard and table piles
        """

        for player in self.players:
            # Get the player input
            action = player.getInput()
            pass
