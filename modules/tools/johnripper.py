from modules.tools.basetool import BaseTool


class JohnTheRipperTool(BaseTool):
    def __init__(self):
        super().__init__("John the Ripper")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running John the Ripper...")
        # Add your John the Ripper-specific functionality here