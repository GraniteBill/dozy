#!/bin/bash
check_for_package(){
	if dpkg-query -s "$1" 1>/dev/null 2>&1; then
    		return 0 # package is installed
	else
		return 1 # package is not installed
	fi
}

if check_for_package "python3"; then
	echo "Python 3 is Installed"
else
	echo "Python 3 is Not Installed"
    echo "Installing Python 3"
    sudo apt-get install python3
fi

if check_for_package "python3-pip"; then
	echo "Python 3 Pip is Installed"
else
	echo "Python 3 Pip is Not Installed"
    echo "Installing Python 3 Pip"
    sudo apt-get install python3-pip
fi

if check_for_package "terminator"; then
	echo "terminator is Installed"
else
	echo "terminator is Not Installed"
    echo "Installing terminator"
    sudo apt-get install terminator
fi

if check_for_package "gcc"; then
    echo "gcc Installed"
else
    echo "gcc is Not Installed"
    echo "Installing gcc"
    sudo apt-get install gcc
fi

if check_for_package "gobuster"; then
    echo "Gobuster Installed"
else
    echo "Gobuster is Not Installed"
    echo "Installing Gobuster"
    sudo apt-get install gobuster
fi
