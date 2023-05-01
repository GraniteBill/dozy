import os
import subprocess
from modules.tools.basetool import BaseTool

class NmapTool(BaseTool):
    def __init__(self):
        super().__init__("Nmap")
        self.nmap_options = [
            ("-p", "Specify ports or port ranges to scan"),
            ("-sS", "Syn scan, a stealthy port scanning technique"),
            ("-sU", "UDP scan, for scanning UDP ports"),
            ("-sV", "Version detection, for identifying the versions of services running on the target"),
            ("-O", "OS detection, for identifying the target's operating system"),
            ("-sn", "Ping scan, for discovering live hosts without scanning ports"),
            ("-T", "Timing template, for adjusting the speed of the scan"),
            ("-oN", "Save output in normal human-readable format"),
            ("-oX", "Save output in XML format"),
            ("-oG", "Save output in grepable format"),
            ("-v", "Verbose mode, for increased output detail"),
            ("-q", "Quiet mode, for reduced output detail"),
            ("-A", "Aggressive scan, for enabling OS detection, version detection, script scanning, and traceroute"),
        ]
        self.handle_menu()

    def print_nmap_options(self):
        for idx, (tag, description) in enumerate(self.nmap_options, start=1):
            print(f"{idx}. {tag}: {description}")

    def print_options(self):
        print("1. Verbose scan ")
        print("2. Quiet scan")
        print("3. Recommended general scan")
        print("4. Custom scan")
        print("5. Back to Tools Menu")

    def handle_choice(self, choice):
        if choice == '1':
            self.verbose_scan()
        elif choice == '2':
            self.quiet_scan()
        elif choice == '3':
            self.general_scan()
        elif choice == '4':
            self.custom_scan()
        elif choice == '5':
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.handle_menu()

    def handle_menu(self):
        while True:
            self.print_options()
            choice = input("> ")
            self.handle_choice(choice)

    def run_scan(self, options):
        print("Running Nmap...")
        target_ip = input("Enter the target IP address: ")
        outputfile = input("Enter the output file name: ")
        command = f"nmap {options} {target_ip} -oA {outputfile}"
        print(f"Running command: {command}")

        terminal_command = f"xdg-open 'terminal://{command}'"
        subprocess.Popen(terminal_command, shell=True)
        input("Press Enter to return to the tools menu...")
        self.exit()

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")


    def verbose_scan(self):
        options = "-v -sS -A"
        self.run_scan(options)

    def quiet_scan(self):
        options = "-q -sS -A"
        self.run_scan(options)

    def general_scan(self):
        options = "-sS -sV -O"
        self.run_scan(options)

    def custom_scan(self):
        print("Available Nmap options:")
        self.print_nmap_options()
        options = input("Enter custom Nmap options: ")
        self.run_scan(options)


if __name__ == "__main__":
    NmapTool()

