from dataclasses import dataclass

# удар: сколько урона и был ли он критическим
@dataclass(frozen=True)
class Hit:
    damage: int
    critical: bool
