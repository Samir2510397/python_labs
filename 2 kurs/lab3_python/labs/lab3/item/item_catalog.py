from __future__ import annotations
from ..core.unknown_code_error import UnknownCodeError
from .armor import Armor
from .item import Item
from .weapon import Weapon

# каталог хранит шаблоны предметов, а наружу отдает только их копии
class ItemCatalog:

    def __init__(self) -> None:
        self._prototypes: dict[str, Item] = {}

    def register(self, prototype: Item) -> None:
        self._prototypes[prototype.code] = prototype

    # каталог не знает, какой конкретно класс у шаблона - копию создает сам шаблон
    def create(self, code: str) -> Item:
        prototype = self._prototypes.get(code)
        if prototype is None:
            raise UnknownCodeError("Предмет", code)

        return prototype.copy()

    def create_weapon(self, code: str) -> Weapon:
        item = self.create(code)
        if isinstance(item, Weapon):
            return item

        raise ValueError(f"Предмет '{code}' не является оружием")

    def create_armor(self, code: str) -> Armor:
        item = self.create(code)
        if isinstance(item, Armor):
            return item

        raise ValueError(f"Предмет '{code}' не является броней")

    @property
    def codes(self) -> list[str]:
        return list(self._prototypes)
