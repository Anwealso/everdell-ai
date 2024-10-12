"""
game.py
Alex Nicholson
11/08/2024

This is the everdell game that holds all of the game state and input actions 
and state transitions.
"""

from random import random
from Player import Player


class Game:
    def __init__(self, num_players=2):
        """
        Inits the everdell game class

        Args:
            - All of the game args
        """
        random.seed()
        self.round_count = 0
        self.gameover = False
        self.players = [
            Player(str(random.randint(0, 999))) for player in range(num_players)
        ]

    def run(self):
        """
        Runs the whole game
        """

        while not self.gameover:
            print(f"======= ROUND {self.round_count+1} =======")
            self.step()
            self.round_count += 1

            if self.round_count > 2:
                self.gameover = True

        print("Game over, XXX wins.")

    def step(self):
        """
        Step the game state

        Gets player input from the player and handle the transfre of cards and
        resources to/from the discard and table piles
        """
        for player in self.players:
            # Get the player input
            action = player.get_action()
            print(f"Action: {action.value}")
