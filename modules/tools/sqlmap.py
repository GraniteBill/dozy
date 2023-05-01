from modules.tools.basetool import BaseTool


class SqlmapTool(BaseTool):
    def __init__(self):
        super().__init__("Sqlmap")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running Sqlmap...")
        # Add your Sqlmap-specific functionality here