"""
game.py
Alex Nicholson
11/08/2024

This is the everdell game that holds all of the game state and input actions 
and state transitions.
"""

from random import random
from Player import Player
from Deck import Deck
from Cards.Card import Card, get_deck
from ActionSpaces.ForestActionSpace import ForestActionSpace


class Game:
    def __init__(self, num_players=2):
        """
        Inits the everdell game

        Args:
            - All of the game args
        """
        random.seed()
        self.round_count = 0
        self.gameover = False
        self.main_deck: Deck = Deck(get_deck())
        self.players = [
            Player(player_id, self.main_deck.takeRandomCards(5 + player_id))
            for player_id in range(num_players)
        ]
        # self.forest: list[Card] = random.choice(ForestActionSpace.all_forest_cards(), 4)
        self.meadow: list[Card] = self.main_deck.takeRandomCards(4)

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
