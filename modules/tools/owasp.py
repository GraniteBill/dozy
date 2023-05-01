from modules.tools.basetool import BaseTool


class OwaspZapTool(BaseTool):
    def __init__(self):
        super().__init__("OWASP ZAP")
        self.print_options()
        choice = input("> ")
        self.handle_choice(choice)

    def run_tool(self):
        print("Running OWASP ZAP...")
        # Add your OWASP ZAP-specific functionality here