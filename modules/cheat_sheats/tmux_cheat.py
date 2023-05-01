class TmuxCheatSheet:
    def __init__(self, callback=None):
        self.print_cheat_sheet()
        self.callback = callback

    def print_cheat_sheet(self):
        cheat_sheet = '''
tmux Cheat Sheet

Session Management
==================
tmux new-session -s <session-name>        Create new session
tmux attach-session -t <session-name>     Attach to a session
tmux switch-client -n                     Switch to next session
tmux switch-client -p                     Switch to previous session
tmux list-sessions                        List all sessions
tmux detach                               Detach from the current session (Prefix + d)
tmux kill-session -t <session-name>       Kill a session

Window Management
=================
tmux new-window                           Create a new window (Prefix + c)
tmux select-window -t <window-number>     Switch to a specific window (Prefix + <window-number>)
tmux rename-window <new-name>             Rename the current window (Prefix + ,)
tmux list-windows                         List all windows in the current session
tmux next-window                          Switch to the next window (Prefix + n)
tmux previous-window                      Switch to the previous window (Prefix + p)
tmux swap-window -t <window-number>       Swap the current window with another window
tmux link-window -s <session>:<window>    Link a window from another session
tmux unlink-window                        Unlink the current window
tmux kill-window                          Kill the current window (Prefix + &)

Pane Management
===============
tmux split-window                         Split the current pane horizontally (Prefix + %)
tmux split-window -v                      Split the current pane vertically (Prefix + ")
tmux select-pane -t <pane-number>         Switch to a specific pane (Prefix + <arrow-keys>)
tmux swap-pane -t <pane-number>           Swap the current pane with another pane
tmux kill-pane                            Kill the current pane (Prefix + x)
tmux resize-pane -t <pane-number> -x <width> -y <height>  Resize a specific pane (Prefix + <arrow-keys> (with Ctrl))
tmux setw synchronize-panes on/off        Synchronize input to all panes (Prefix + <space>)

General Commands
================
tmux list-commands                        List all available tmux commands
tmux info                                 Show information about the current session
tmux capture-pane                         Capture the contents of the current pane
tmux paste-buffer                         Paste the contents of the most recent buffer (Prefix + ])
tmux save-buffer <file>                   Save the contents of a buffer to a file
tmux show-buffer                          Show the contents of the most recent buffer
tmux list-buffers                         List all buffers
tmux delete-buffer -b <buffer>            Delete a specific buffer

Note: Most tmux commands can be executed by pressing the "Prefix" key (Ctrl-b by default) followed by the command key.
'''
        print(cheat_sheet)
        input("\nPress Enter to return to cheat sheets menu...")
        self.exit()
    
    def exit(self):
        if self.callback:
            self.callback(0)
        else:
            print("Exiting...")

if __name__ == "__main__":
    TmuxCheatSheet()
