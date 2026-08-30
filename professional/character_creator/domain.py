from dataclasses import dataclass, replace
from enum import StrEnum


class Stat(StrEnum):
    CONSTITUTION = "constitucion"
    STRENGTH = "fuerza"
    DEXTERITY = "destreza"
    INTELLIGENCE = "inteligencia"
    CHARISMA = "carisma"


class CharacterClass(StrEnum):
    PALADIN = "paladin"
    THIEF = "ladron"
    MAGE = "mago"
    VIKING = "vikingo"


CLASS_BONUSES: dict[CharacterClass, Stat] = {
    CharacterClass.PALADIN: Stat.CONSTITUTION,
    CharacterClass.THIEF: Stat.DEXTERITY,
    CharacterClass.MAGE: Stat.INTELLIGENCE,
    CharacterClass.VIKING: Stat.STRENGTH,
}


@dataclass(frozen=True)
class CharacterStats:
    constitution: int
    strength: int
    dexterity: int
    intelligence: int
    charisma: int

    def with_bonus(self, stat: Stat, bonus: int) -> "CharacterStats":
        field_by_stat = {
            Stat.CONSTITUTION: "constitution",
            Stat.STRENGTH: "strength",
            Stat.DEXTERITY: "dexterity",
            Stat.INTELLIGENCE: "intelligence",
            Stat.CHARISMA: "charisma",
        }
        field_name = field_by_stat[stat]
        return replace(self, **{field_name: getattr(self, field_name) + bonus})


@dataclass(frozen=True)
class Character:
    name: str
    age: int
    character_class: CharacterClass
    stats: CharacterStats
