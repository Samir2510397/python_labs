from __future__ import annotations
import copy
from abc import ABC, abstractmethod
from .enchantment import Enchantment

class Item(ABC):

    def __init__(self, code: str, name: str, base_price: int) -> None:
        # код шаблона, из которого получен предмет
        self._code = code
        self._name = name
        self._base_price = base_price
        self._enchantments: list[Enchantment] = []

    def copy(self) -> Item:
        # copy.copy создает объект того же класса, что и оригинал, с теми же значениями полей,
        # поэтому копировать умеет любой наследник, и переопределять этот метод им не нужно
        clone = copy.copy(self)
        # но копия поверхностная: поля копии ссылаются на те же объекты, что и у оригинала,
        # поэтому список зачарований заменяем на новый, иначе копия и оригинал делили бы его
        clone._enchantments = list(self._enchantments)
        return clone

    # какие зачарования подходят этому предмету
    @property
    @abstractmethod
    def possible_enchantments(self) -> tuple[Enchantment, ...]: ...

    # описание характеристик предмета, например "урон 12"
    @property
    @abstractmethod
    def description(self) -> str: ...

    def enchant(self, enchantment: Enchantment) -> None:
        if enchantment not in self.possible_enchantments:
            raise ValueError(f"Зачарование '{enchantment.name}' не подходит для предмета '{self._name}'")

        self._enchantments.append(enchantment)

    @property
    def code(self) -> str:
        return self._code

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> int:
        return self._base_price + sum(enchantment.bonus_price for enchantment in self._enchantments)

    @property
    def enchantments(self) -> tuple[Enchantment, ...]:
        return tuple(self._enchantments)
