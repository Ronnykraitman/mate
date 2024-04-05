#!/usr/bin/env python3
import signal
from utils import goodbye, welcome, show_menu
from fun.fun_mate import fun_mate
from mac.mac_mate import mac_mate
from system.system_mate import sys_mate


def signal_handler(signal, frame):
    goodbye()


general_mate_options = [
    ("Mac Magic Tools", mac_mate),
    ("System Assistant", sys_mate),
    ("Entertain me", fun_mate),
    ("Exit", goodbye)
]


def mate():
    try:
        show_menu(general_mate_options, "Here's what I can do:")
    except Exception as e:
        print(f"Oh No! Something went wrong: {e}")


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    welcome()
    mate()



