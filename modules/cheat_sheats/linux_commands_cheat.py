from frontend.banner import Banner


class LinuxCommandLineCheatSheet:
    def __init__(self, callback=None):
        self.print_cheat_sheet()
        self.callback = callback

    def print_cheat_sheet(self):
        Banner()
        print("Linux Command Line Cheat Sheet:\n")

        print("File Operations:")
        print("  Command       Description")
        print("  ===========   ==============================")
        print("  ls            List directory contents")
        print("  cd            Change directory")
        print("  pwd           Print working directory")
        print("  mkdir         Make a new directory")
        print("  rm            Remove files or directories")
        print("  cp            Copy files or directories")
        print("  mv            Move files or directories")
        print("  cat           Display file content")
        print("  chmod         Change file permissions")
        print("  chown         Change file ownership")

        print("\nProcess Management:")
        print("  Command       Description")
        print("  ===========   ==============================")
        print("  ps            Display active processes")
        print("  top           Display real-time process information")
        print("  kill          Terminate a process")

        print("\nNetworking:")
        print("  Command       Description")
        print("  ===========   ==============================")
        print("  ifconfig      Display network interface configuration")
        print("  ip            Display network interface configuration (newer)")
        print("  netstat       Display network connections and routing tables")
        print("  ping          Test network connectivity")
        print("  traceroute    Trace the route to a remote host")

        input("\nPress Enter to return to cheat sheets menu...")
        self.exit()
    
    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")

if __name__ == "__main__":
    LinuxCommandLineCheatSheet()