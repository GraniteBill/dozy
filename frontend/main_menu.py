from frontend.banner import Banner
from frontend.cheat_sheet_menu import CheatSheetMenu
from frontend.tools_menu import ToolsMenu



class MainMenu:
    def __init__(self):
        self.tools = [
            {"name": "Tools Menu", "class": ToolsMenu},
            {"name": "Cheat Sheets Menu", "class": CheatSheetMenu},
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
        print("\n99. Exit")

    def handle_choice(self, choice):
        try:
            choice = int(choice)
            if 1 <= choice <= 10:
                tool = self.tools[choice - 1]
                tool['class']()
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

