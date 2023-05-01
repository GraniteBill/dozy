from modules.tools.basetool import BaseTool


class HydraTool(BaseTool):
    def __init__(self):
        super().__init__("Hydra")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running Hydra...")
        # Add your Hydra-specific functionality here