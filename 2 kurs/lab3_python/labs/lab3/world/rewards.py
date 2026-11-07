from __future__ import annotations
from dataclasses import dataclass
from ..item.item import Item

# итоги экспедиции для героя;# gold отрицательный, если герой проиграл и потерял золото, loot равен None, если добычи нет
@dataclass(frozen=True)
class Rewards:
    experience: int
    gold: int
    loot: Item | None
    levels_gained: int
