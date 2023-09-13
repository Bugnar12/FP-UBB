from src.domain.table import Table
from src.domain.movesymbol import MoveSymbol
from src.domain.validator import MoveValidator
from src.controller.controller import TableService
from src.userinterface.userinterface import UserInterface
from src.controller.controller import TableService


def main():

    initial_table = Table()
    move_validator = MoveValidator()
    table_service = TableService(initial_table, move_validator)
    interface = UserInterface(table_service)

    interface.run_game()


if __name__ == "__main__":
    main()
