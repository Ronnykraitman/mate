from utils import get_response_from_bash_command, run_bash_command


def get_wifi_password():
    wifi_network_name: str = input("\nWhat is the wifi network name: ")
    password, error = get_response_from_bash_command(f"security find-generic-password -wa {wifi_network_name}")
    if password:
        print(f"The password for {wifi_network_name} is: {password}")


def get_ip_address():
    address, error = get_response_from_bash_command("ifconfig en0 | grep -w inet | awk '{ print $2 }'")
    print(f"Your IP address is: {address}")


def get_command_info():
    command_to_info: str = input("\nWhat is the command name you'd like to learn about: ")
    run_bash_command(f"man {command_to_info}")


def get_traceroute():
    website_address: str = input("\nWhat is the website address you want to trace: ")
    run_bash_command(f"traceroute {website_address}")


def dig_website():
    website_address: str = input("\nWhat is the website address you want dig into: ")
    run_bash_command(f"dig {website_address}")


def get_top_cpu_use():
    run_bash_command("top")


def get_top_memory_use():
    run_bash_command(f"top -o rsize")


def kill_process():
    port_to_kill = input("Port number you want to get rid off: ")
    run_bash_command(f"kill -TERM {port_to_kill}")


def mac_uptime():
    run_bash_command("uptime")


def time_to_leave():
    print("Set an alarm to tell you its time to stop using te terminal and get a rest\n")
    ttl = input("When should I alert you? (format: 1245): ")
    run_bash_command(f"leave {ttl}")
