from __future__ import annotations
from .enchantment import FOR_ARMOR, Enchantment
from .item import Item
# больше этой доли урона никакая броня не поглощает
MAX_DEFENSE = 0.75

# броня поглощает долю входящего урона
class Armor(Item):

    def __init__(self, code: str, name: str, base_price: int, defense: float) -> None:
        super().__init__(code, name, base_price)
        self._defense = defense

    # доля поглощаемого урона с учетом зачарований
    @property
    def defense(self) -> float:
        total = self._defense + sum(enchantment.bonus_defense for enchantment in self.enchantments)
        return min(total, MAX_DEFENSE)

    @property
    def possible_enchantments(self) -> tuple[Enchantment, ...]:
        return FOR_ARMOR

    @property
    def description(self) -> str:
        return f"защита {round(self.defense * 100)}%"
