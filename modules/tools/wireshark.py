import subprocess
import time
from frontend.banner import Banner
from modules.tools.basetool import BaseTool


class WiresharkTool(BaseTool):
    def __init__(self, callback=None):
        super().__init__("Wireshark", self.handle_choice)
        self.callback = callback
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def print_options(self):
        Banner()
        print("1. Launch Wireshark")
        print("2. Back to Tools Menu")

    def handle_choice(self, choice):
        if choice == '1':
            self.run_tool()
        elif choice == '2':
            self.exit()
        else:
            print("Invalid choice. Please try again.")
            self.handle_menu()

    def handle_menu(self):
        while True:
            self.print_options()
            choice = input("> ")
            self.handle_choice(choice)

    def run_tool(self):
        print("Running Wireshark...")
        command = "wireshark"
        terminal_command = f"{command} &> /dev/null &"
        subprocess.Popen(terminal_command, shell=True)
        input("Press Enter to return to the tools menu...")
        self.exit()

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")
        


if __name__ == "__main__":
    WiresharkTool()
