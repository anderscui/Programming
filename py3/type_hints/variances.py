# coding=utf-8
from typing import TypeVar, Generic


class Beverage:
    """Any beverage"""


class Juice(Beverage):
    """Any fruit juice."""


class OrangeJuice(Juice):
    """Delicious juice"""


T = TypeVar('T')
T_co = TypeVar('T_co', covariant=True)


class BeverageDispenser(Generic[T_co]):
    def __init__(self, beverage: T_co):
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]):
    """Install a fruit juice dispenser"""


class Refuse:
    """Any refuse."""


class Biodegradable(Refuse):
    """Biodegradable refuse."""


class Compostable(Biodegradable):
    """Compostable refuse."""


T_contra = TypeVar('T_contra', contravariant=True)


class TrashCan(Generic[T_contra]):

    def put(self, refuse: T_contra) -> None:
        """Store trash until dumped."""


def deploy(trash_can: TrashCan[Biodegradable]):
    """Deploy a trash can for biodegradable refuse."""


if __name__ == '__main__':
    # For T = TypeVar('T')
    # Argument 1 to "install" has incompatible type "BeverageDispenser[OrangeJuice]";
    # expected "BeverageDispenser[Juice]"  [arg-type]
    # for T_co = TypeVar('T_co', covariant=True), it's OK
    orange_juice_dispenser = BeverageDispenser(OrangeJuice())
    install(orange_juice_dispenser)

    # refuse is ok
    trash_can = TrashCan[Refuse]()
    deploy(trash_can)

    # Argument 1 to "deploy" has incompatible type "TrashCan[Compostable]";
    # expected "TrashCan[Biodegradable]"  [arg-type]
    compost_can = TrashCan[Compostable]()
    deploy(compost_can)
