#!/usr/bin/env python3

from utils import goodbye, show_menu
from mac.functions import show_info, delete_trash, stay_awake, discover_ports, mac_uptime, kill_process

mac_mate_options = [
    ("Display your mac info", show_info),
    ("Have a full trash can? lets clean it", delete_trash),
    ("Force mac to stay awake as long as you need it", stay_awake),
    ("Discover ports", discover_ports),
    ("Kill and slaughter any process", kill_process),
    ("How much time your mac is awake?", mac_uptime),
    ("Main Menu", ()),
    ("Exit", goodbye)
]


def mac_mate():
    print("Let me show you some cool mac tricks:\n")
    while True:
        show_menu(mac_mate_options, "Here are some tricks:")
