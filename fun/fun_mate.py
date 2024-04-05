from utils import goodbye, show_menu
from fun.functions import game_hub, play_tetris, matrix_saver, aquarium_saver, play_nsnake, play_spaceinvaders, \
    play_greed, play_cataclysm

fun_mate_options = [
    ("External Game Hub", game_hub),
    ("Play Tetris", play_tetris),
    ("Enter the matrix", matrix_saver),
    ("Dive with the fish", aquarium_saver),
    ("Play the old good snake", play_nsnake),
    ("Play terminal space invaders", play_spaceinvaders),
    ("Play Greed", play_greed),
    ("Play Cataclysm", play_cataclysm),
    ("Main Menu", ()),
    ("Exit", goodbye)
]


def fun_mate():
    print("Lets get you entertained, shall we?\n")
    while True:
        show_menu(fun_mate_options, "Fun options:")
