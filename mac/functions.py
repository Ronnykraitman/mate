# !/usr/bin/env python3
import socket

from simple_term_menu import TerminalMenu
from utils import run_bash_command


def delete_trash():
    print("\nCleaning your trash....\n")
    run_bash_command("rm -rf ~/.Trash/*")


def show_info():
    run_bash_command("system_profiler SPHardwareDataType")


def stay_awake():
    print("Setting Mac to stay awake until you press ^C\n")
    run_bash_command("caffeinate")


def discover_ports():
    host: str = input("The default address is 'localhost'. Give me a different one if you like or just press Enter: ")
    if not host:
        host: str = "localhost"
    ports_as_str: str = input("Type any ports you'd like, comma seperated: ")
    ports_as_list: list = ports_as_str.split(",")
    open_ports: list = []
    for port in ports_as_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, int(port)))
        if result == 0:
            open_ports.append(port)

    if open_ports:
        print(f"Here are the open ports: ", open_ports)
        terminal_menu = TerminalMenu(["Yes", "No"], title="Would you like me to kill them?")
        terminal_menu.show()
        entry_name = terminal_menu.chosen_menu_entry
        if entry_name == "Yes":
            print("OK, lets kill some ports\n")
            kill_process(open_ports)
        else:
            print("Your are merciful\n")

    else:
        print("No open port\n")


def kill_process(port_to_kill: list = None):
    if not port_to_kill:
        ports_to_kill_as_str: str = input("Port numbers you want to get rid off, comma seperated: ")
        ports_as_list: list = ports_to_kill_as_str.split(",")
        for ps in ports_as_list:
            run_bash_command(f"kill -TERM {ps}")
        print()


def mac_uptime():
    run_bash_command("uptime")
