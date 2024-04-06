from utils import goodbye, show_menu
from system.functions import get_wifi_password, get_ip_address, get_command_info, get_traceroute, dig_website, \
    get_top_cpu_use, get_top_memory_use, time_to_leave

sys_mate_options = [
    ("Display any historical wifi network password", get_wifi_password),
    ("Discover you IP address", get_ip_address),
    ("Learn about any cli command", get_command_info),
    ("Trace any website route", get_traceroute),
    ("Dig deeper into any website dns", dig_website),
    ("See processes by CPU usage", get_top_cpu_use),
    ("See processes by Memory usages", get_top_memory_use),
    ("Set alarm to let you know when it time to leave the terminal", time_to_leave),
    ("Main Menu", ()),
    ("Exit", goodbye)
]


def sys_mate():
    print("Discover your system from under the hood:\n")
    while True:
        show_menu(sys_mate_options, "Some under the hood stuff:")
