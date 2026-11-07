from abc import ABC, abstractmethod
from ..item.armor import Armor
from ..item.weapon import Weapon

# Абстрактная фабрика: стартовый набор снаряжения
class StarterKitFactory(ABC):

    # возвращает некое оружие
    @abstractmethod
    def create_weapon(self) -> Weapon: ...

    # возвращает некую броню
    @abstractmethod
    def create_armor(self) -> Armor: ...
