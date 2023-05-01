from modules.tools.basetool import BaseTool


class AircrackNgTool(BaseTool):
    def __init__(self):
        super().__init__("Aircrack-ng")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running Aircrack-ng...")
        # Add your Aircrack-ng-specific functionality here