import random
from collections.abc import Callable


STAT_NAMES = (
    "constitucion",
    "fuerza",
    "destreza",
    "inteligencia",
    "carisma",
)

CLASS_BONUSES = {
    "paladin": "constitucion",
    "ladron": "destreza",
    "mago": "inteligencia",
    "vikingo": "fuerza",
}


def roll_stats(roll: Callable[[int, int], int] = random.randint) -> dict[str, int]:
    return {stat_name: roll(1, 10) for stat_name in STAT_NAMES}


def apply_class_bonus(stats: dict[str, int], character_class: str) -> dict[str, int]:
    stats_with_bonus = stats.copy()
    bonus_stat = CLASS_BONUSES[character_class]
    stats_with_bonus[bonus_stat] += 6
    return stats_with_bonus


def create_character(
    name: str,
    age: int,
    character_class: str,
    roll: Callable[[int, int], int] = random.randint,
) -> dict[str, str | int | dict[str, int]]:
    stats = roll_stats(roll)
    final_stats = apply_class_bonus(stats, character_class)

    return {
        "name": name,
        "age": age,
        "class": character_class,
        "stats": final_stats,
    }


def ask_character_name() -> str:
    return input("Ingrese el nombre del personaje: ").strip()


def ask_character_age() -> int:
    return int(input("Ingrese la edad del personaje: "))


def ask_character_class() -> str:
    print("Escribe tu clase entre estas cuatro:")
    print("paladin: +6 constitución")
    print("ladron: +6 destreza")
    print("mago: +6 inteligencia")
    print("vikingo: +6 fuerza")
    return input(": ").strip().lower()


def display_character(character: dict[str, str | int | dict[str, int]]) -> None:
    stats = character["stats"]
    assert isinstance(stats, dict)

    print()
    print("Muy bien, estos son tus datos")
    print(f"Nombre: {character['name']}")
    print(f"Edad: {character['age']}")
    print(f"Clase: {character['class']}")

    for stat_name, value in stats.items():
        print(f"{stat_name}: {value}")


def run_game() -> None:
    name = ask_character_name()
    age = ask_character_age()
    character_class = ask_character_class()

    if character_class not in CLASS_BONUSES:
        print("¡Clase no válida!")
        return

    character = create_character(name, age, character_class)

    print(f"Has escogido {character_class}")
    print("Vamos a tirar los dados de tus estadísticas")
    display_character(character)


if __name__ == "__main__":
    run_game()
