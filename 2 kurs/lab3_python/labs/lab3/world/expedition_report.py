from dataclasses import dataclass
from ..combat.battle_report import BattleReport
from .rewards import Rewards

# отчет об экспедиции: с каким сидом, куда, как прошел бой и что получил герой
@dataclass(frozen=True)
class ExpeditionReport:
    seed: int
    location_code: str
    battle: BattleReport
    rewards: Rewards
