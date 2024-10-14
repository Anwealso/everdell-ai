from Player import Player
from ActionSpaces.ActionSpace import ActionSpace


class CardActionSpace(ActionSpace):

    def __init__(self, isOpen: bool, useEffect: function) -> None:
        self.isOpen: bool = isOpen
        super(useEffect)

    def hasAvailableSlot(self, player: Player) -> bool:
        """
        Checks whether the actionspace has an available slot for this specific player
        """
        return len(self.workers) == 0 and (self.isOpen or (self in player.playedCards))
