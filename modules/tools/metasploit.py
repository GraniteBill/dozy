from modules.tools.basetool import BaseTool
import subprocess


class MetasploitTool(BaseTool):
    def __init__(self, callback=None):
        super().__init__("Metasploit", self.handle_choice)
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def print_options(self):
        print("1. Launch msfconsole")
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
        print("Running Metasploit...")
        command = "msfconsole"
        terminal_command = f"xfce4-terminal --hold --execute bash -c '{command}; read -n 1 -s -r -p \"Press any key to continue...\"'"
        subprocess.Popen(terminal_command, shell=True)
        input("Press Enter to return to the main menu...")
        self.exit()

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")


if __name__ == "__main__":
    MetasploitTool()
