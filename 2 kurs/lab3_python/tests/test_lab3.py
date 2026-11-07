import subprocess
import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path

from labs.lab3.camp.merchant import Merchant
from labs.lab3.combat.event_type import EventType
from labs.lab3.combat.outcome import Outcome
from labs.lab3.combat.side import Side
from labs.lab3.core.dice import Dice
from labs.lab3.core.unknown_code_error import UnknownCodeError
from labs.lab3.enemy.dragon import Dragon
from labs.lab3.enemy.goblin import Goblin
from labs.lab3.enemy.skeleton import Skeleton
from labs.lab3.hero.hero import Hero
from labs.lab3.hero.hero_class import HeroClass
from labs.lab3.item.armor import Armor
from labs.lab3.item.bow import Bow
from labs.lab3.item.default_catalog import (
    CHAINMAIL, DAWN_BLADE, DRAGONSCALE_ARMOR, IRON_SWORD, create_default_catalog,
)
from labs.lab3.item.enchantment import FIERY, WARDING
from labs.lab3.item.staff import Staff
from labs.lab3.item.sword import Sword
from labs.lab3.world.crypt import Crypt
from labs.lab3.world.dragon_lair import DragonLair
from labs.lab3.world.forest import Forest
from labs.lab3.world.location_registry import LocationRegistry


class Lab3Tests(unittest.TestCase):
    def setUp(self):
        self.catalog = create_default_catalog()

    def hero(self, hero_class=HeroClass.WARRIOR, level=1, gold=50):
        return (Hero.Builder().set_name('Артур').set_hero_class(hero_class)
                .set_starter_kit(hero_class.starter_kit(self.catalog))
                .set_level(level).set_gold(gold).build())

    def test_singleton_identity(self):
        self.assertIs(Dice(), Dice())

    def test_dice_reseed_repeats_sequence(self):
        d = Dice()
        d.reseed(7)
        first = [d.roll(1, 100) for _ in range(20)]
        d.reseed(7)
        self.assertEqual(first, [d.roll(1, 100) for _ in range(20)])

    def test_prototype_isolates_enchantments(self):
        first = self.catalog.create(IRON_SWORD)
        second = first.copy()
        second.enchant(FIERY)
        self.assertIsNot(first, second)
        self.assertEqual(first.enchantments, ())
        self.assertEqual(second.damage, first.damage + 6)
        self.assertEqual(self.catalog.create(IRON_SWORD).enchantments, ())

    def test_enchantment_is_frozen(self):
        with self.assertRaises(FrozenInstanceError):
            FIERY.bonus_damage = 100

    def test_wrong_enchantment_rejected(self):
        with self.assertRaises(ValueError):
            self.catalog.create(IRON_SWORD).enchant(WARDING)

    def test_abstract_factory_families(self):
        for hero_class, weapon_type, defense in (
            (HeroClass.WARRIOR, Sword, 0.3),
            (HeroClass.RANGER, Bow, 0.2),
            (HeroClass.MAGE, Staff, 0.1),
        ):
            with self.subTest(hero_class=hero_class):
                kit = hero_class.starter_kit(self.catalog)
                self.assertIsInstance(kit.create_weapon(), weapon_type)
                self.assertIsInstance(kit.create_armor(), Armor)
                self.assertEqual(kit.create_armor().defense, defense)
                self.assertIsNot(kit.create_weapon(), kit.create_weapon())

    def test_builder_defaults_and_formulas(self):
        hero = self.hero(level=3)
        self.assertEqual((hero.health, hero.gold, hero.experience_to_next_level), (150, 50, 300))
        self.assertEqual(hero.roll_damage().damage, 18)

    def test_builder_rejects_invalid_fields(self):
        for builder in (
            Hero.Builder(),
            Hero.Builder().set_name('Артур'),
            Hero.Builder().set_name('Артур').set_hero_class(HeroClass.WARRIOR),
            Hero.Builder().set_name('x' * 21),
            Hero.Builder().set_name('Артур').set_hero_class(HeroClass.WARRIOR)
                .set_starter_kit(HeroClass.WARRIOR.starter_kit(self.catalog)).set_level(0),
            Hero.Builder().set_name('Артур').set_hero_class(HeroClass.WARRIOR)
                .set_starter_kit(HeroClass.WARRIOR.starter_kit(self.catalog)).set_gold(-1),
        ):
            with self.subTest(builder=builder), self.assertRaises(ValueError):
                builder.build()

    def test_factory_method_creates_different_enemies(self):
        for location_type, enemy_type in ((Forest, Goblin), (Crypt, Skeleton), (DragonLair, Dragon)):
            with self.subTest(location=location_type):
                location = location_type(self.catalog)
                self.assertIsInstance(location._create_enemy(), enemy_type)
                self.assertIsNot(location._create_enemy(), location._create_enemy())

    def test_expedition_is_reproducible_for_same_initial_state(self):
        first = Forest(self.catalog).explore(self.hero(), seed=7)
        second = Forest(self.catalog).explore(self.hero(), seed=7)
        self.assertEqual(first.battle, second.battle)
        self.assertEqual(first.rewards.gold, second.rewards.gold)
        self.assertEqual(first.rewards.experience, second.rewards.experience)

    def test_victory_rewards_and_death_events(self):
        hero = self.hero(level=3)
        report = Forest(self.catalog).explore(hero, seed=7)
        self.assertEqual(report.battle.outcome, Outcome.VICTORY)
        self.assertEqual(hero.gold, 50 + report.rewards.gold)
        self.assertEqual(hero.experience, 40)
        self.assertEqual(report.battle.events[-1].type, EventType.DEATH)
        self.assertEqual(report.battle.events[-1].target, Side.ENEMY)
        self.assertTrue(all(event.target_health_after >= 0 for event in report.battle.events))

    def test_defeat_loses_half_gold(self):
        hero = self.hero(gold=51)
        report = DragonLair(self.catalog).explore(hero, seed=7)
        self.assertEqual(report.battle.outcome, Outcome.DEFEAT)
        self.assertEqual((hero.gold, report.rewards.gold, report.rewards.experience), (26, -25, 0))
        self.assertIsNone(report.rewards.loot)

    def test_experience_can_raise_multiple_levels(self):
        hero = self.hero()
        self.assertEqual(hero.gain_experience(350), 2)
        self.assertEqual((hero.level, hero.experience, hero.experience_to_next_level), (3, 50, 300))

    def test_defense_cap_and_minimum_damage(self):
        armor = self.catalog.create_armor(CHAINMAIL)
        for _ in range(20):
            armor.enchant(WARDING)
        self.assertEqual(armor.defense, 0.75)
        hero = self.hero()
        hero.add_item(armor)
        hero.equip(armor)
        self.assertEqual(hero.receive_hit(1), 1)

    def test_equipment_returns_old_item_to_inventory(self):
        hero = self.hero()
        old = hero.weapon
        new = self.catalog.create_weapon(IRON_SWORD)
        hero.add_item(new)
        hero.equip(new)
        self.assertIs(hero.weapon, new)
        self.assertIn(old, hero.inventory)
        self.assertNotIn(new, hero.inventory)

    def test_merchant_buy_sell_and_equipped_rejection(self):
        hero = self.hero(gold=1000)
        merchant = Merchant(self.catalog, [IRON_SWORD])
        item = merchant.buy(hero, IRON_SWORD)
        self.assertIn(item, hero.inventory)
        self.assertEqual(hero.gold, 1000 - item.price)
        price = merchant.sell(hero, item)
        self.assertEqual(hero.gold, 1000 - item.price + price)
        with self.assertRaises(ValueError):
            merchant.sell(hero, hero.weapon)

    def test_insufficient_funds_leave_state_unchanged(self):
        hero = self.hero(gold=0)
        merchant = Merchant(self.catalog, [IRON_SWORD])
        with self.assertRaises(ValueError):
            merchant.buy(hero, IRON_SWORD)
        self.assertEqual((hero.gold, hero.inventory), (0, ()))

    def test_unknown_codes_raise(self):
        registry = LocationRegistry([Forest(self.catalog)])
        for action in (
            lambda: self.catalog.create('missing'),
            lambda: registry.get('missing'),
            lambda: HeroClass.by_code('missing'),
        ):
            with self.subTest(action=action), self.assertRaises(UnknownCodeError):
                action()

    def test_progression_from_start_to_dragon_victory(self):
        hero = self.hero()
        forest = Forest(self.catalog)
        for seed in range(100):
            forest.explore(hero, seed=seed)
            if hero.level >= 5:
                break
        self.assertGreaterEqual(hero.level, 5)
        for code in (DAWN_BLADE, DRAGONSCALE_ARMOR):
            item = self.catalog.create(code)
            hero.add_item(item)
            hero.equip(item)
        report = DragonLair(self.catalog).explore(hero, seed=7)
        self.assertEqual(report.battle.outcome, Outcome.VICTORY)

    def test_console_creation_expedition_and_exit(self):
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, '-m', 'labs.lab3.main'], cwd=root,
            input='1\nСамир\n1\n1\n0\n', text=True,
            encoding='utf-8', capture_output=True, timeout=10,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('Самир разбивает лагерь', result.stdout)
        self.assertIn('Гоблин', result.stdout)


if __name__ == '__main__':
    unittest.main(verbosity=2)
