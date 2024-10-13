from enum import Enum
from resources import ResourceValue


class ResourceValue:
    def __init__(self, twig, resin, pebble, berry) -> None:
        self.twig = twig
        self.resin = resin
        self.pebble = pebble
        self.berry = berry
        pass

    def __add__(self, other_value: ResourceValue):
        return ResourceValue(
            self.twig + other_value.twig,
            self.resin + other_value.resin,
            self.pebble + other_value.pebble,
            self.berry + other_value.berry,
        )

    def __sub__(self, other_value: ResourceValue):
        result_twig: int = self.twig - other_value.twig
        result_resin: int = self.resin - other_value.resin
        result_pebble: int = self.pebble - other_value.pebble
        result_berry: int = self.berry - other_value.berry

        if result_twig < 0 or result_resin < 0 or result_pebble < 0 or result_berry < 0:
            raise Exception(
                "Error: Subtraction would result in negative resource value"
            )
        else:
            return ResourceValue(result_twig, result_resin, result_pebble, result_berry)

    def sum(self):
        return self.twig + self.resin + self.pebble + self.berry


class ResourceType(Enum):
    TWIG = 1
    RESIN = 2
    PEBBLE = 3
    BERRY = 4
