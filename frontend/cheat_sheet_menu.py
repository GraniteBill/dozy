
from frontend.banner import Banner
from modules.cheat_sheats.common_ports_cheat import CommonPortsAndProtocolsCheatSheet
from modules.cheat_sheats.linux_commands_cheat import LinuxCommandLineCheatSheet
from modules.cheat_sheats.reverse_shell_cheat import ReverseShellCheatSheet
from modules.cheat_sheats.tmux_cheat import TmuxCheatSheet


class CheatSheetMenu:
    def __init__(self):
        self.tools = [
            {"name": "Reverse Shells", "class": ReverseShellCheatSheet},
            {"name": "Linux Commands", "class": LinuxCommandLineCheatSheet},
            {"name": "Tmux", "class": TmuxCheatSheet},
            {"name": "Common Ports and Protocols", "class": CommonPortsAndProtocolsCheatSheet},
        ]
        
        self.handle_input()
        

    def handle_input(self):
        self.print_menu()
        choice = input("> ")
        self.handle_choice(choice)

    def print_menu(self):
        Banner()
        print("Choose your selection from the menu below:\n")
        for i, tool in enumerate(self.tools, 1):
            print(f"{i}. {tool['name']}")
        print("\n99. Back to Main Menu")

    def handle_choice(self, choice):
        try:
            choice = int(choice)
            if 1 <= choice <= 10:
                tool = self.tools[choice - 1]
                tool['class'](callback=self.handle_choice)
            elif choice == 99:
                self.exit()
            elif choice == 0:
                self.handle_input()
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice. Please try again.")
            input("Press enter to continue...")
            self.__init__()

    def exit(self):
        print("Exiting the program...")
        return

