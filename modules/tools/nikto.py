from modules.tools.basetool import BaseTool


class NiktoTool(BaseTool):
    def __init__(self):
        super().__init__("Nikto")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running Nikto...")
        # Add your Nikto-specific functionality here