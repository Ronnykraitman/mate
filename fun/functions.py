from simple_term_menu import TerminalMenu
from utils import run_bash_command


def game_hub():
    print("\nMy creator have a game hub repository. Would you like me to clone it for you?")
    terminal_menu = TerminalMenu(["Yes", "No"], title="Clone Game Hub Repo?")
    terminal_menu.show()
    entry_name = terminal_menu.chosen_menu_entry
    if entry_name == "Yes":
        print("Cloning....")
        run_bash_command("gh repo clone Ronnykraitman/pygame")
    else:
        print("Ok then, clone it at your own time: 'https://github.com/Ronnykraitman/pygame'")


def matrix_saver():
    run_bash_command("cmatrix")


def play_tetris():
    run_bash_command("tetris")


def aquarium_saver():
    run_bash_command("asciiquarium")


def play_nsnake():
    run_bash_command("nsnake")


def play_spaceinvaders():
    run_bash_command("spaceinvaders")


def play_greed():
    run_bash_command("greed")


def play_cataclysm():
    run_bash_command("cataclysm")
