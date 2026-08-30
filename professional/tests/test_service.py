import pytest

from character_creator.domain import CharacterClass, CharacterStats
from character_creator.service import create_character, roll_stats


def fixed_roll(minimum: int, maximum: int) -> int:
    return 5


def test_roll_stats_uses_roll_for_every_stat() -> None:
    rolled_values = iter((1, 2, 3, 4, 5))
    calls: list[tuple[int, int]] = []

    def roll(minimum: int, maximum: int) -> int:
        calls.append((minimum, maximum))
        return next(rolled_values)

    stats = roll_stats(roll)

    assert stats == CharacterStats(
        constitution=1,
        strength=2,
        dexterity=3,
        intelligence=4,
        charisma=5,
    )
    assert calls == [(1, 10)] * 5


@pytest.mark.parametrize(
    ("character_class", "expected_stats"),
    [
        (
            CharacterClass.PALADIN,
            CharacterStats(
                constitution=11,
                strength=5,
                dexterity=5,
                intelligence=5,
                charisma=5,
            ),
        ),
        (
            CharacterClass.THIEF,
            CharacterStats(
                constitution=5,
                strength=5,
                dexterity=11,
                intelligence=5,
                charisma=5,
            ),
        ),
        (
            CharacterClass.MAGE,
            CharacterStats(
                constitution=5,
                strength=5,
                dexterity=5,
                intelligence=11,
                charisma=5,
            ),
        ),
        (
            CharacterClass.VIKING,
            CharacterStats(
                constitution=5,
                strength=11,
                dexterity=5,
                intelligence=5,
                charisma=5,
            ),
        ),
    ],
)
def test_create_character_applies_class_bonus(
    character_class: CharacterClass,
    expected_stats: CharacterStats,
) -> None:
    character = create_character(
        name="Arthas",
        age=30,
        character_class=character_class,
        roll=fixed_roll,
    )

    assert character.name == "Arthas"
    assert character.age == 30
    assert character.character_class is character_class
    assert character.stats == expected_stats
