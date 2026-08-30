from character_creator.cli import run_cli
from character_creator.service import RandomDiceRoller


def main() -> None:
    run_cli(RandomDiceRoller())


if __name__ == "__main__":
    main()
