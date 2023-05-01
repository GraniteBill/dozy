import os


class Banner():
    def __init__(self):
        self.clear_screen()
        self.print_rabbit_run_banner()


    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def print_rabbit_run_banner(self):
        banner = r"""
    ____       _     _     _ _        ____              
    |  _ \ __ _| |__ | |__ (_) |_     |  _ \ _   _ _ __  
    | |_) / _` | '_ \| '_ \| | __|____| |_) | | | | '_ \ 
    |  _ < (_| | |_) | |_) | | ||_____|  _ <| |_| | | | |
    |_| \_\__,_|_.__/|_.__/|_|\__|    |_| \_\\__,_|_| |_|
                                                        
        """
        print(banner)
