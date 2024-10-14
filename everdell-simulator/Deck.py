from Cards.Card import Card
from Cards.Farm import *
from Cards.Carnival import *
from Cards.McGregorsMarket import *
import random


class Deck:
    def __init__(
        self,
        cards: list[Card] = [],
    ):
        self.cards: list[Card] = cards

    def addCard(self, card: Card) -> None:
        self.cards.append(card)

    def addCards(self, cards: list[Card]) -> None:
        self.cards.append(cards)

    def takeRandomCard(self) -> None:
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card

    def takeRandomCards(self, numCards: int) -> None:
        cards = random.sample(self.cards, numCards)
        self.cards.remove(cards)
        return cards


def get_deck() -> Deck:
    """
    Constructs the starting main deck of shuffled cards
    """
    deck: Deck = Deck()

    deck.append(Farm())
    deck.append(Carnival())
    deck.append(McGregorsMarket())

    return deck
