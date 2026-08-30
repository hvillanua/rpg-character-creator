import pytest

from character_creator.domain import CharacterClass, CharacterStats
from character_creator.service import create_character, roll_stats


class FixedDiceRoller:
    def __init__(self, result: int) -> None:
        self.result = result

    def roll(self, minimum: int, maximum: int) -> int:
        return self.result


def test_roll_stats_uses_dice_roller_for_every_stat() -> None:
    dice_roller = FixedDiceRoller(5)

    stats = roll_stats(dice_roller)

    assert stats == CharacterStats(
        constitution=5,
        strength=5,
        dexterity=5,
        intelligence=5,
        charisma=5,
    )


@pytest.mark.parametrize(
    ("character_class", "expected_stats"),
    [
        (CharacterClass.PALADIN, CharacterStats(11, 5, 5, 5, 5)),
        (CharacterClass.THIEF, CharacterStats(5, 5, 11, 5, 5)),
        (CharacterClass.MAGE, CharacterStats(5, 5, 5, 11, 5)),
        (CharacterClass.VIKING, CharacterStats(5, 11, 5, 5, 5)),
    ],
)
def test_create_character_applies_class_bonus(
    character_class: CharacterClass,
    expected_stats: CharacterStats,
) -> None:
    dice_roller = FixedDiceRoller(5)

    character = create_character(
        name="Arthas",
        age=30,
        character_class=character_class,
        dice_roller=dice_roller,
    )

    assert character.name == "Arthas"
    assert character.age == 30
    assert character.character_class is character_class
    assert character.stats == expected_stats
