

class BaseTool:
    def __init__(self, tool_name, callback=None):
        self.tool_name = tool_name
        self.callback = callback

    def print_options(self):
        print(f"{self.tool_name} options:")
        print("1. Run the tool")
        print("2. Back to tools menu")

    def handle_choice(self, choice):
        if self.callback:
            self.callback(choice)
        else:
            print("Invalid choice. Please try again.")


    def run_tool(self):
        raise NotImplementedError("You must implement the run_tool method")
