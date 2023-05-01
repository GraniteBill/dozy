from frontend.banner import Banner



class CommonPortsAndProtocolsCheatSheet:
    def __init__(sel, callback=None):
        self.print_cheat_sheet()
        self.callback = callback

    def print_cheat_sheet(self):
        Banner()
        print("Common Ports and Protocols Cheat Sheet:\n")
        print("  Port(s)  Protocol                          Description")
        print("  =======  ===============================   ===============================")
        print("  20, 21    FTP (File Transfer Protocol)")
        print("  22        SSH (Secure Shell)")
        print("  23        Telnet")
        print("  25        SMTP (Simple Mail Transfer Protocol)")
        print("  53        DNS (Domain Name System)")
        print("  67, 68    DHCP (Dynamic Host Configuration Protocol)")
        print("  69        TFTP (Trivial File Transfer Protocol)")
        print("  80        HTTP (Hypertext Transfer Protocol)")
        print("  110       POP3 (Post Office Protocol 3)")
        print("  119       NNTP (Network News Transfer Protocol)")
        print("  123       NTP (Network Time Protocol)")
        print("  135       MSRPC (Microsoft Remote Procedure Call)")
        print("  139       NetBIOS (NetBIOS Session Service)")
        print("  143       IMAP (Internet Message Access Protocol)")
        print("  161       SNMP (Simple Network Management Protocol)")
        print("  389       LDAP (Lightweight Directory Access Protocol)")
        print("  443       HTTPS (HTTP Secure)")
        print("  445       SMB (Server Message Block)")
        print("  3389      RDP (Remote Desktop Protocol)")
        print("  8080      HTTP Proxy")

        input("\nPress Enter to return to cheat sheets menu...")
        self.exit()

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")
        

if __name__ == "__main__":
    CommonPortsAndProtocolsCheatSheet()



