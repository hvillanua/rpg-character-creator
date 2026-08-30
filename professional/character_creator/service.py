import random
from collections.abc import Callable

from character_creator.domain import CLASS_BONUSES, Character, CharacterClass, CharacterStats


Roll = Callable[[int, int], int]

CLASS_BONUS = 6
MIN_STAT_ROLL = 1
MAX_STAT_ROLL = 10


def roll_stats(roll: Roll) -> CharacterStats:
    return CharacterStats(
        constitution=roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        strength=roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        dexterity=roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        intelligence=roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
        charisma=roll(MIN_STAT_ROLL, MAX_STAT_ROLL),
    )


def create_character(
    name: str,
    age: int,
    character_class: CharacterClass,
    roll: Roll = random.randint,
) -> Character:
    stats = roll_stats(roll).with_bonus(
        CLASS_BONUSES[character_class],
        CLASS_BONUS,
    )

    return Character(
        name=name,
        age=age,
        character_class=character_class,
        stats=stats,
    )
