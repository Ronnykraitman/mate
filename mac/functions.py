# !/usr/bin/env python3
import socket
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
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex(('localhost', 1234))
    if result == 0:
        print("Port is open\n")
    else:
        print("Port is not open\n")
