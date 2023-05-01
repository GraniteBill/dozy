import os
import subprocess
from frontend.banner import Banner
from modules.tools.basetool import BaseTool
from modules.tools.aircrack import AircrackNgTool
from modules.tools.burpsuite import BurpSuiteTool
from modules.tools.hydra import HydraTool
from modules.tools.johnripper import JohnTheRipperTool
from modules.tools.metasploit import MetasploitTool
from modules.tools.nikto import NiktoTool
from modules.tools.nmap import NmapTool
from modules.tools.owasp import OwaspZapTool
from modules.tools.reverse_shell_generator import ReverseShellGenerator
from modules.tools.sqlmap import SqlmapTool
from modules.tools.wireshark import WiresharkTool


class ToolsMenu:
    def __init__(self):
        self.tools = [
            {"name": "Nmap", "class": NmapTool},
            {"name": "Metasploit", "class": MetasploitTool},
            {"name": "Wireshark", "class": WiresharkTool},
            {"name": "Burp Suite", "class": BurpSuiteTool},
            {"name": "John the Ripper", "class": JohnTheRipperTool},
            {"name": "Aircrack-ng", "class": AircrackNgTool},
            {"name": "Hydra", "class": HydraTool},
            {"name": "OWASP ZAP", "class": OwaspZapTool},
            {"name": "Nikto", "class": NiktoTool},
            {"name": "Sqlmap", "class": SqlmapTool},
            {"name": "Reverse Shell", "class": ReverseShellGenerator}
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
            if 1 <= choice <= 98:
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

