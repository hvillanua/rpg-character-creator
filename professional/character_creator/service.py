import random
from typing import Protocol

from character_creator.domain import CLASS_BONUSES, Character, CharacterClass, CharacterStats


CLASS_BONUS = 6
MIN_STAT_ROLL = 1
MAX_STAT_ROLL = 10


class DiceRoller(Protocol):
    def roll(self, minimum: int, maximum: int) -> int:
        ...


class RandomDiceRoller:
    def roll(self, minimum: int, maximum: int) -> int:
        return random.randint(minimum, maximum)


def roll_stats(dice_roller: DiceRoller) -> CharacterStats:
    return CharacterStats(
        constitution=dice_roller.roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        strength=dice_roller.roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        dexterity=dice_roller.roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        intelligence=dice_roller.roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        charisma=dice_roller.roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
    )


def create_character(
    name: str,
    age: int,
    character_class: CharacterClass,
    dice_roller: DiceRoller,
) -> Character:
    stats = roll_stats(dice_roller)
    bonus_stat = CLASS_BONUSES[character_class]
    stats = stats.with_bonus(bonus_stat, CLASS_BONUS)

    return Character(
        name=name,
        age=age,
        character_class=character_class,
        stats=stats,
    )
