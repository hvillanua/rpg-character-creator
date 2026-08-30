from character_creator import apply_class_bonus, create_character, roll_stats


def always_roll_five(minimum: int, maximum: int) -> int:
    return 5


def always_roll_three(minimum: int, maximum: int) -> int:
    return 3


def test_roll_stats() -> None:
    stats = roll_stats(always_roll_five)

    assert stats == {
        "constitucion": 5,
        "fuerza": 5,
        "destreza": 5,
        "inteligencia": 5,
        "carisma": 5,
    }


def test_paladin_bonus() -> None:
    stats = {
        "constitucion": 5,
        "fuerza": 5,
        "destreza": 5,
        "inteligencia": 5,
        "carisma": 5,
    }

    result = apply_class_bonus(stats, "paladin")

    assert result["constitucion"] == 11
    assert result["fuerza"] == 5
    assert result["destreza"] == 5
    assert result["inteligencia"] == 5
    assert result["carisma"] == 5


def test_each_class_bonus() -> None:
    class_bonuses = {
        "paladin": "constitucion",
        "ladron": "destreza",
        "mago": "inteligencia",
        "vikingo": "fuerza",
    }

    for character_class, bonus_stat in class_bonuses.items():
        stats = {
            "constitucion": 1,
            "fuerza": 1,
            "destreza": 1,
            "inteligencia": 1,
            "carisma": 1,
        }

        result = apply_class_bonus(stats, character_class)

        assert result[bonus_stat] == 7


def test_create_character() -> None:
    character = create_character("Gandalf", 100, "mago", always_roll_three)

    assert character["name"] == "Gandalf"
    assert character["age"] == 100
    assert character["class"] == "mago"
    assert character["stats"] == {
        "constitucion": 3,
        "fuerza": 3,
        "destreza": 3,
        "inteligencia": 9,
        "carisma": 3,
    }


def run_tests() -> None:
    test_roll_stats()
    test_paladin_bonus()
    test_each_class_bonus()
    test_create_character()
    print("Todos los tests han pasado.")


if __name__ == "__main__":
    run_tests()
