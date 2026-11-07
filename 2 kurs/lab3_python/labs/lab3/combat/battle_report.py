from __future__ import annotations
from dataclasses import dataclass
from .battle_event import BattleEvent
from .outcome import Outcome
from .participant import Participant

# результат боя: кто сражался, чем все закончилось и что происходило по ходу дела
@dataclass(frozen=True)
class BattleReport:
    hero: Participant
    enemy: Participant
    outcome: Outcome
    events: tuple[BattleEvent, ...]
