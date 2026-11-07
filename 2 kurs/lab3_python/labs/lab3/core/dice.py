from __future__ import annotations
import random
from typing import Sequence, TypeVar
T = TypeVar("T")

# Одиночка: общий источник случайности на всю игру
class Dice:

    # единственный экземпляр класса
    _instance: Dice | None = None

    _random: random.Random

    # __new__ вызывается при каждом Dice() еще до создания объекта:
    # если экземпляр уже есть, возвращаем его, а не создаем новый
    def __new__(cls) -> Dice:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._random = random.Random()

        return cls._instance

    # после установки сида все последующие броски повторяются в точности
    def reseed(self, seed: int) -> None:
        self._random.seed(seed)

    # случайный сид
    def next_seed(self) -> int:
        return self._random.randrange(1_000_000)

    # случайное целое число от low до high включительно
    def roll(self, low: int, high: int) -> int:
        return self._random.randint(low, high)

    # возвращает True с вероятностью probability (от 0 до 1)
    def chance(self, probability: float) -> bool:
        return self._random.random() < probability

    # случайный элемент последовательности
    def pick(self, options: Sequence[T]) -> T:
        return self._random.choice(options)
