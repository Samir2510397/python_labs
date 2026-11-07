from __future__ import annotations
from enum import Enum
from ..core.unknown_code_error import UnknownCodeError
from ..item.item_catalog import ItemCatalog
from ..kit.mage_kit_factory import MageKitFactory
from ..kit.ranger_kit_factory import RangerKitFactory
from ..kit.starter_kit_factory import StarterKitFactory
from ..kit.warrior_kit_factory import WarriorKitFactory

class HeroClass(Enum):

    # значение каждого класса: код, название, стартовое здоровье и класс фабрики стартового набора
    WARRIOR = ("warrior", "Воин", 120, WarriorKitFactory)
    RANGER = ("ranger", "Следопыт", 100, RangerKitFactory)
    MAGE = ("mage", "Маг", 85, MageKitFactory)

    def __init__(self, code: str, display_name: str, base_health: int, kit_factory: type[StarterKitFactory]) -> None:
        self.code = code
        self.display_name = display_name
        self.base_health = base_health
        self._kit_factory = kit_factory

    # каждый класс сам знает свою фабрику стартового снаряжения
    def starter_kit(self, catalog: ItemCatalog) -> StarterKitFactory:
        return self._kit_factory(catalog)

    @classmethod
    def by_code(cls, code: str) -> HeroClass:
        for hero_class in cls:
            if hero_class.code == code:
                return hero_class

        raise UnknownCodeError("Класс героя", code)
