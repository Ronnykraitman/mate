import subprocess

from simple_term_menu import TerminalMenu


def run_bash_command(command: str):
    subprocess.run([command], shell=True)


def get_response_from_bash_command(command: str):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    return output, error


def create_options_menu(options: list):
    options_to_display = []
    for i, entry in enumerate(options):
        options_to_display.append(f"[⭑] {entry[0]}")
    return options_to_display


def show_menu(options: list, menu_title: str):
    options_for_display = create_options_menu(options)
    terminal_menu = TerminalMenu(options_for_display, title=menu_title)
    menu_entry_index = terminal_menu.show()
    entry_name = terminal_menu.chosen_menu_entry
    if entry_name == "Main Menu":
        from mate import mate
        mate()
    else:
        options[menu_entry_index][1]()


def welcome():
    name, error = get_response_from_bash_command("whoami")
    print(f"\nHey {name.title()}I'm Mate, your personal assistant\n")
    w1: str = f"say Hey {name.title()}"
    process = subprocess.Popen(w1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    process.communicate()
    w2: str = "say I am mate, your personal assistant"
    process = subprocess.Popen(w2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    process.communicate()
    print("How can I help you?\n")
    run_bash_command("say How can I help you")


def goodbye():
    exit("\nSee you later, buddy 👋")
