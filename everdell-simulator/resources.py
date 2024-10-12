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
        self.twig += other_value.twig
        self.resin += other_value.resin
        self.pebble += other_value.pebble
        self.berry += other_value.berry

    def __sub__(self, other_value: ResourceValue):
        if self.twig >= other_value.twig:
            self.twig -= other_value.twig
        else:
            raise Exception(
                "Error: Subtraction would result in negative resource balance"
            )

        if self.resin >= other_value.resin:
            self.resin -= other_value.resin
        else:
            raise Exception(
                "Error: Subtraction would result in negative resource balance"
            )

        if self.pebble >= other_value.pebble:
            self.pebble -= other_value.pebble
        else:
            raise Exception(
                "Error: Subtraction would result in negative resource balance"
            )

        if self.berry >= other_value.berry:
            self.berry -= other_value.berry
        else:
            raise Exception(
                "Error: Subtraction would result in negative resource balance"
            )


class ResourceType(Enum):
    TWIG = 1
    RESIN = 2
    PEBBLE = 3
    BERRY = 4
