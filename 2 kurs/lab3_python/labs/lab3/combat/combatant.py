from __future__ import annotations
from abc import ABC, abstractmethod
from .hit import Hit

# всё, что может участвовать в бою: и герой, и враги
class Combatant(ABC):

    # код вида сущности: класс героя или тип врага
    @property
    @abstractmethod
    def code(self) -> str: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def health(self) -> int: ...

    @property
    @abstractmethod
    def max_health(self) -> int: ...

    @abstractmethod
    def is_alive(self) -> bool: ...

    # удар, который будет нанесен данной сущностью
    @abstractmethod
    def roll_damage(self) -> Hit: ...

    # получение удара, возвращает урон, который прошел на самом деле
    @abstractmethod
    def receive_hit(self, damage: int) -> int: ...
