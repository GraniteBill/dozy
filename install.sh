#!/bin/bash


# Global variables
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
NC='\033[0m'


echo -e "${YELLOW}Setting up config file.${NC}"
sudo python3 config.py

echo -e "${YELLOW}Installing Necessary Dependencies and Tools.${NC}"
echo

sudo apt-get update
./check_packages.sh

if [ -d /opt/discover/.git ]; then
    echo -e "${BLUE}Updating Discover.${NC}"
    cd /opt/discover/
    git pull
    ./update.sh
    echo
else
    echo -e "${YELLOW}Installing Discover.${NC}"
    git clone https://github.com/leebaird/discover.git /opt/discover/
    cd /opt/discover/
    ./update.sh
    echo

fi


if [ -d /opt/airgeddon/.git ]; then
    echo -e "${BLUE}Updating Airgeddon.${NC}"
    cd /opt/airgeddon/
    git pull
    echo
else
    echo -e "${YELLOW}Installing Airgeddon.${NC}"
    git clone https://github.com/v1s1t0r1sh3r3/airgeddon.git /opt/airgeddon/
    echo
fi

if [ -d /opt/fluxion/.git ]; then
    echo -e "${BLUE}Updating Fluxion.${NC}"
    cd /opt/fluxion/
    git pull
    echo
else
    echo -e "${YELLOW}Installing Fluxion.${NC}"
    git clone https://github.com/FluxionNetwork/fluxion.git /opt/fluxion/
    echo
fi

if [ -d /opt/scapy/.git ]; then
    echo -e "${BLUE}Updating Scapy.${NC}"
    cd /opt/scapy/
    git pull
    sudo python3 setup.py install
    echo
else
    echo -e "${YELLOW}Installing Scapy.${NC}"
    git clone https://github.com/phaethon/scapy /opt/scapy/
    cd /opt/scapy/
    sudo python3 setup.py install
    echo
fi

echo "${BLUE} Setting up empire database. ${NC}"
cd /opt/Empire/setup
python setup_database.py



if [ -d /opt/xerxes/.git ]; then
    echo -e "${BLUE}Updating Xerxes.${NC}"
    cd /opt/xerxes/
    git pull
    gcc xerxes.c -o xerxes
    echo
else
    echo -e "${YELLOW}Installing Xerxes.${NC}"
    git clone https://github.com/zanyarjamal/xerxes.git /opt/xerxes/
    cd /opt/xerxes
    gcc xerxes.c -o xerxes
fi

if [ -d /opt/anonsurf/.git ]; then
    echo -e "${BLUE}Updating Anonsurf.${NC}"
    cd /opt/anonsurf/
    git pull
    ./installer.sh
    echo
else
    echo -e "${YELLOW}Installing Anonsurf.${NC}"
    git clone https://github.com/Und3rf10w/kali-anonsurf.git /opt/anonsurf/
    cd /opt/anonsurf/
    ./installer.sh
    echo
fi

if [ -d /opt/hcxtools/.git ]; then
    echo -e "${BLUE}Updating HCXTools.${NC}"
    cd /opt/hcxtools/
    git pull
    make
    make install
    echo
else
    echo -e "${YELLOW}Installing HCXTools.${NC}"
    git clone https://github.com/ZerBea/hcxtools /opt/hcxtools/
    cd /opt/hcxtools/
    make
    make install
    echo
fi

if [ -d /opt/hcxdumptool/.git ]; then
    echo -e "${BLUE}Updating HCXDumpTool.${NC}"
    cd /opt/hcxdumptool/
    git pull
    make
    make install
    echo
else
    echo -e "${YELLOW}Installing HCXDumpTool.${NC}"
    git clone https://github.com/ZerBea/hcxdumptool /opt/hcxdumptool/
    cd /opt/hcxdumptool/
    make
    make install
    echo
fi

if [-d /opt/routersploit/.git]; then
 	echo -e "${BLUE}Updating Routersploit.${NC}"
	sudo git pull
else
 	echo -e "${YELLOW}Installing Routersploit.${NC}"
	sudo git clone https://www.github.com/threat9/routersploit /opt/routersploit
	cd /opt/routersploit/
	sudo apt-get install libglib2.0-dev
	sudo python3 -m pip install bluepy
	sudo python3 -m pip install -r requirements.txt
fi

echo
echo
