from character_creator.domain import Character, CharacterClass
from character_creator.service import DiceRoller, create_character


def ask_name() -> str:
    while True:
        name = input("Ingrese el nombre del personaje: ").strip()
        if name:
            return name
        print("El nombre no puede estar vacío.")


def ask_age() -> int:
    while True:
        value = input("Ingrese la edad del personaje: ").strip()

        try:
            age = int(value)
        except ValueError:
            print("La edad debe ser un número.")
            continue

        if age <= 0:
            print("La edad debe ser mayor que cero.")
            continue

        return age


def ask_character_class() -> CharacterClass:
    print("Elige una clase:")

    for character_class in CharacterClass:
        print(f"- {character_class.value}")

    while True:
        value = input(": ").strip().lower()

        try:
            return CharacterClass(value)
        except ValueError:
            print("Clase no válida. Inténtalo de nuevo.")


def display_character(character: Character) -> None:
    stats = character.stats

    print()
    print("Muy bien, estos son tus datos")
    print(f"Nombre: {character.name}")
    print(f"Edad: {character.age}")
    print(f"Clase: {character.character_class.value}")
    print(f"Constitución: {stats.constitution}")
    print(f"Fuerza: {stats.strength}")
    print(f"Destreza: {stats.dexterity}")
    print(f"Inteligencia: {stats.intelligence}")
    print(f"Carisma: {stats.charisma}")


def run_cli(dice_roller: DiceRoller) -> None:
    name = ask_name()
    age = ask_age()
    character_class = ask_character_class()

    character = create_character(
        name=name,
        age=age,
        character_class=character_class,
        dice_roller=dice_roller,
    )

    display_character(character)
