import subprocess
from modules.tools.basetool import BaseTool

class Gobuster(BaseTool):
    def __init__(self):
        super().__init__("GoBuster")
        self.wordlists = [
            "/usr/share/wordlists/dirb/common.txt",
            "/usr/share/wordlists/dirbuster/directory-list-2.3-small.txt",
            "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt",
            "/usr/share/wordlists/rockyou.txt"
        ]
        self.handle_menu()

    def print_options(self):
        print("1. Directory/File Brute-Forcing")
        print("2. DNS Subdomain Brute-Forcing")
        print("3. Virtual Host Brute-Forcing")
        print("4. URL Parameter Brute-Forcing")
        print("5. Custom GoBuster Command")
        print("6. Back to Tools Menu")

    def handle_choice(self, choice):
        if choice == '1':
            self.directory_bruteforce()
        elif choice == '2':
            self.dns_subdomain_bruteforce()
        elif choice == '3':
            self.virtual_host_bruteforce()
        elif choice == '4':
            self.url_parameter_bruteforce()
        elif choice == '5':
            self.custom_gobuster()
        elif choice == '6':
            exit()
        else:
            print("Invalid choice. Please try again.")
            self.handle_menu()

    def handle_menu(self):
        while True:
            self.print_options()
            choice = input("> ")
            self.handle_choice(choice)

    def print_wordlists(self):
        print("Select a wordlist:")
        for idx, wordlist in enumerate(self.wordlists, start=1):
            print(f"{idx}. {wordlist}")

    def select_wordlist(self):
        self.print_wordlists()
        choice = int(input("> "))
        return self.wordlists[choice - 1]

    def run_gobuster(self, options):
        wordlist = self.select_wordlist()
        target_url = input("Enter the target URL: ")
        command = f"gobuster {options} -w {wordlist} -u {target_url}"
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

    def directory_bruteforce(self):
        options = "dir"
        self.run_gobuster(options)

    def dns_subdomain_bruteforce(self):
        options = "dns -i"
        self.run_gobuster(options)

    def virtual_host_bruteforce(self):
        options = "vhost"
        self.run_gobuster(options)

    def url_parameter_bruteforce(self):
        options = "urls"
        self.run_gobuster(options)

    def custom_gobuster(self):
        options = input("Enter custom GoBuster options: ")
        self.run_gobuster(options)


if __name__ == "__main__":
    Gobuster()
