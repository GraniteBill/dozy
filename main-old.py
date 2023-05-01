import os
import glob
import csv
import argparse
import subprocess
import json
import random
from requests import get
import time
import re
import configparser

wlan_interface = ""
eth_interface = ""

def main():
    global wlan_interface, eth_interface
    try:
        print_banner()
        print_menu()
        x = input("> ")
        if x == "if":
            subprocess.call("ifconfig", shell = "True")
        elif x == "iw":
            subprocess.call("iwconfig", shell = "True")
        elif x == "mon":
            enable_monitor_mode()
        elif x == "man":
            enable_managed_mode()
        elif x == "1":
            change_mac()
        elif x == "d1":
            print("[+] Restoring MAC Address")
            restore_mac()
        elif x == "v1":
            show_mac()
        elif x == "2":
            my_ip = get('https://api.ipify.org').text
            print("[+] Public IP Address: "+my_ip)
        elif x == "3":
            ip = input("Please enter ip address > ")
            loc = get('http://api.ipstack.com/'+ip+'?access_key=25b479d1d4148636cb00035b087ddbf9&format=1').text
            json_file = json.loads(loc)
            print("Country: "+json_file['country_name'])
            try:
                print("City: "+json_file['city'])
            except:
                print("[-] Uanble to locate city")
            try:
                print("Latitude: "+str(json_file['latitude']))
                print("Longitude: "+str(json_file['longitude']))
            except:
                print("[-] Unable to get latitide and longitude")
        elif x == "4":
            try:
                print("[+] Enabling IP Forwarding")
                subprocess.call("sudo echo \"1\" > /proc/sys/net/ipv4/ip_forward", shell = "True")
                print("[+] IP Forwarding Enabled")
            except:
                print("[-] Enabling IP Forwarding Failed")
        elif x == "d4":
            try:
                print("[+] Disabling IP Forwarding")
                subprocess.call("sudo echo \"0\" > /proc/sys/net/ipv4/ip_forward", shell = "True")
                print("[+] IP Forwarding Disabled")
            except:
                print("[-] Disabling IP Forwarding Failed")
        elif x == "7":
            target_ip = input("Enter Target IP > ")
            #gateway_ip = input("Enter Gateway IP > ")
            set_random_mac()
            time.sleep(2)
            subprocess.call("sudo python3 ~/Dozy/Code/arp_spoof.py "+ target_ip +" wlan0", shell = "True")
        elif x == "7":
            print("Mass Scan Not Implemented")
        elif x == "8":
            print("DNS Spoof Not Implemented")
        elif x == "9":
            enable_monitor_mode()
            wifi()
        elif x == "anon":
            anonsurf()
        elif x == "air":
            airgeddon()
        elif x == "fl":
            run_fluxion()
        elif x == "wi":
            subprocess.call("sudo terminator --profile=Persistant --maximise --command=\"wifite --kill\"", shell = "True")
        elif x == "burp":
            print("[+] Loading Burpsuite")
            run_burpsuite()
            print("[+] Burpsuite loaded")
        elif x == "xer":
            run_xerxes()
        elif x == "msf":
            subprocess.call("sudo terminator --profile=Non-Persistant --maximise --command=\"msfconsole\"", shell = "True")
        elif x == "wir":
            subprocess.call("sudo wireshark &", shell = "True")
        elif x == "dis":
            run_discover()
        elif x == "emp":
            run_empire()
        elif x == "config":
            redo_config()
        elif x == "pin":
            pineapple()
        elif x == "zen":
            subprocess.call("sudo zenmap &", shell = "True")
        elif x == "x" or x == "exit":
            exit(0)
        elif x == "5":
            nmap()
        elif x == "nord":
            nord()
        else:
            y = input("[-] Unrecognized input execute (x) or return to  main menu (enter) >")
            if y == "":
                main()
            else:
                subprocess.call(x, shell = "True")

        new_input = input("Enter to return to main menu > ")
        if new_input == "":
            main()
        elif new_input == "exit" or new_input == "x":
            exit(0)

    except KeyboardInterrupt:
        print("\n[+] Please type exit(x) and press enter to close console")
        time.sleep(2)
        main()

def print_menu():
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<29s}{:<0s}'.format('|-','-'*30,'-'*30,'|'+'-'*30,'-'*29,'|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','Commands','','| Tools','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<29s}{:<0s}'.format('|-','-'*30,'-'*30,'|'+'-'*30,'-'*29,'|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ',' if. ifconfig',' iw. iwconfig','|  msf. Metasploit','  emp. Empire','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','mon. monitor mode','man. managed mode','|  xer. Xerxes','   fl. Fluxion','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  1. change MAC',' d1. restore MAC','|  wir. Wireshark','  zen. Zenmap','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ',' v1. view MAC','','| burp. Burpsuite','  pin. Pineapple','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  2. public IP','  3. geolocate IP','|  dis. Discover','   wi. Wifite','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  4. enable IP forwarding',' d4. disable IP forwarding','| nord. NordVPN',' anon. Anonsurf','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ',' f4. flush IP tables','','| air. Airgeddon','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  5. nmap scans','  6. mass scan','|','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  7. arp spoof','  8. dns spoof','|','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  9. wifi','','|','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<30s}{:<0s}'.format('| ','  config. Set Config','','|','','|'))
    print('{:>0s}{:<30s}{:<30s}{:<30s}{:<29s}{:<0s}'.format('|-','-'*30,'-'*30,'|'+'-'*30,'-'*29,'|'))

def print_banner():
    global wlan_interface, eth_interface
    subprocess.call("clear", shell = "True")
    logo = r"""
   ██████╗  ██████╗ ███████╗██╗   ██╗
   ██╔══██╗██╔═══██╗╚══███╔╝╚██╗ ██╔╝
   ██║  ██║██║   ██║  ███╔╝  ╚████╔╝ 
   ██║  ██║██║   ██║ ███╔╝    ╚██╔╝  
   ██████╔╝╚██████╔╝███████╗   ██║   
   ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝  
    """
    print(logo)
    config = configparser.ConfigParser()
    config.read('Config/config.ini')
    wlan_interface = config['DEFAULT']['wlan_interface']
    eth_interface =  config['DEFAULT']['eth_interface']
    print('Wireless Interface: '+wlan_interface)
    print('Ethernet Interface: '+eth_interface)
    print("")

def enable_managed_mode():
    global wlan_interface, eth_interface
    print("[+] Enabling managed mode for interface "+wlan_interface)
    subprocess.call("sudo ifconfig "+wlan_interface+" down", shell = "True")
    subprocess.call("sudo iwconfig "+wlan_interface+" mode managed", shell = "True")
    subprocess.call("sudo ifconfig "+wlan_interface+" up", shell = "True")
    subprocess.call("sudo service network-manager restart", shell = "True")
    print("[+] Managed mode for interface "+wlan_interface+" enabled")

def enable_monitor_mode():
    global wlan_interface, eth_interface
    print("[+] Enabling monitor mode for interface "+wlan_interface)
    subprocess.call("sudo airmon-ng check kill", shell = "False")
    subprocess.call("sudo ifconfig "+wlan_interface+" down", shell = "True")
    subprocess.call("sudo iwconfig "+wlan_interface+" mode monitor", shell = "True")
    subprocess.call("sudo ifconfig "+wlan_interface+" up", shell = "True")
    print("[+] Monitor mode for interface "+wlan_interface+" enabled")

def connect_anonsurf():
    subprocess.call("sudo anonsurf start", shell = "True")

def disconnect_anonsurf():
    subprocess.call("sudo anonsurf stop", shell = "True")

def restart_anonsurf():
    subprocess.call("sudo anonsurf restart", shell = "True")

def status_anonsurf():
    subprocess.call("sudo anonsurf status", shell = "True")

def run_discover():
    subprocess.call("sudo terminator --maximise --profile=Persistant --command=\"cd /opt/discover/; ./discover.sh\"", shell = "True")

def run_xerxes():
    website = input("Please enter website to DOS > ")
    command = "\"cd /opt/xerxes/; ./xerxes "+website+" 80;\"";
    subprocess.call("sudo terminator --profile=Non-Persistant --command="+command, shell = "True")

def run_burpsuite():
    subprocess.call("sudo terminator --profile=Non-Persistant --command=\"burpsuite\"", shell = "True")

def run_fluxion():
    subprocess.call("sudo terminator --profile=Non-Persistant --maximise --command=\"cd /opt/fluxion/; ./fluxion.sh;\" ", shell = "True")
    #subprocess.call("bash ../Hacking_Tools/fluxion/fluxion.sh", shell = "True")

def run_empire():
    subprocess.call("sudo terminator --profile=Non-Persistant --maximise --command=\"cd /opt/Empire/; ./empire;\" ", shell =    "True")

def show_mac():
    subprocess.call("sudo macchanger --show " + interface, shell = "False")

def restore_mac():
    subprocess.call("sudo ifconfig "+interface+" down", shell = "False")
    subprocess.call("sudo macchanger --permanent " + interface, shell = "False")
    subprocess.call("sudo ifconfig "+interface+" up", shell = "False")

def set_random_mac():
    subprocess.call("sudo ifconfig "+interface+" down", shell = "False")
    subprocess.call("sudo macchanger -r "+interface, shell = "False")
    subprocess.call("sudo ifconfig "+interface+" up", shell = "False")

def change_mac():
    choice = input("Random (r) or Specific (s) MAC > ")
    if choice == "r" or choice == "random" or choice == "Random":
        subprocess.call("sudo ifconfig "+interface+" down", shell = "False")
        subprocess.call("sudo macchanger -r "+interface, shell = "False")
        subprocess.call("sudo ifconfig "+interface+" up", shell = "False")

    elif choice == "s" or choice == "specific" or choice == "Sepcific":
        new_mac = input("Enter MAC > ")
        subprocess.call("sudo ifconfig "+interface+" down", shell = "False")
        subprocess.call("sudo macchanger -m "+new_mac+" "+interface, shell = "False")
        subprocess.call("sudo ifconfig "+interface+" up", shell = "False")

def airgeddon():
    subprocess.call("sudo terminator --profile=Non-Persistant --maximise --command=\"sudo bash /opt/airgeddon/airgeddon.sh\" ", shell = "True")

def nord():
    nord_menu()
    x = eval(input(">"))
    if x == 1:
        connect_nord()
    elif x == 2:
        disconnect_nord()
    elif x == 3:
        nord_status()
    elif x == 4:
        main()
    else:
        print("Unregonised Input.")
    new_input = input("Press enter to return to Nord menu or 4 to go back to main menu > ")
    if new_input == "4":
        main()
    else:
        nord()

def nord_menu():
    print_banner()
    print("1. Connect NordVPN")
    print("2. Disconnect NordVPN")
    print("3. NordVPN Status")
    print("4. Back")


def connect_nord():
    print("[+] Connect NordVPN")
    subprocess.call("nordvpn connect", shell = "True")


def disconnect_nord():
    print("[+] Disconnecting NordVPN")
    subprocess.call("nordvpn disconnect", shell = "True")

def nord_status():
    subprocess.call("nordvpn status", shell = "True")

def wifi_menu():
    print_banner()
    config = configparser.ConfigParser()
    config.read('Config/config.ini')
    bssid = config['DEFAULT']['bssid']
    channel =  config['DEFAULT']['channel']
    essid = config['DEFAULT']['essid']
    print("Selected Network: "+essid)
    print("BSSID: "+bssid)
    print("Channel: "+channel)
    print("")
    print("1. Scan For Target Network")
    print("2. DDoS")
    print("3. Handshake Capture")
    print("4. Handshake Crack")
    print("5. Back")

def wifi():
    wifi_menu()
    x = eval(input(">"))
    if x == 1:
        scan_networks()
    elif x == 2:
        print("DDoS")
    elif x == 5:
        enable_managed_mode()
        main()
    else:
         print("Unregonised Input.")
    new_input = input("Press enter to return to wifi menu or 6 to go back to main menu > ")
    if new_input == "5":
        enable_managed_mode()
        main()
    else:
        wifi()

def scan_networks():
    global wlan_interface, eth_interface
    try:
        subprocess.call("sudo airodump-ng -w Scans/scan --output-format csv "+ wlan_interface, shell = "True")
        config = configparser.ConfigParser()
        config.read('Config/config.ini')

    except KeyboardInterrupt:
        list_of_files = glob.glob('Scans/*') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        latest_file = latest_file+""
        value = re.search('[^scan-][^\.csv]', latest_file)
        if value is not None:
            value = value[0]
        config = configparser.ConfigParser()
        config.read('Config/config.ini')
        config['DEFAULT']['scan'] = value
        with open('Config/config.ini', 'w') as configfile:
            config.write(configfile)
        #Save file
        print_results()
        netwok = input("Select target: ")

def print_results():
    subprocess.call("clear",shell = "True")
    config = configparser.ConfigParser()
    config.read('Config/config.ini')
    scan = config['DEFAULT']['scan']
    with open('Scans/scan-'+scan+'.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            print(line_count, end = " ")
            print('{:<15}  {:<15}  {:<20} {:<25}'.format(*row))

def anonsurf():
    anonsurf_menu()
    x = eval(input(">"))
    if x == 1:
        connect_anonsurf()
    elif x == 2:
        disconnect_anonsurf()
    elif x == 3:
        status_anonsurf()
    elif x == 4:
        restart_anonsurf()
    elif x == 5:
        main()
    else:
        print("Unregonised Input.")
    new_input = input("Press enter to return to anonsurf menu or 5 to go back to main menu > ")
    if new_input == "5":
        main()
    else:
        anonsurf()

def anonsurf_menu():
    print_banner()
    print("1. Connect Anonsurf")
    print("2. Disconnect Anonsurf")
    print("3. Anonsurf Status")
    print("4. Restart Anonsurf")
    print("5. Back")

def pineapple_menu():
    print_banner()
    print("1. Setup Internet")
    print("2. Open GUI")
    print("3. SSH into Pineapple")
    print("4. Back")

def pineapple():
    pineapple_menu()
    x = eval(input(">"))
    if x == 1:
        print("[+] Downloading wp6.sh")
        subprocess.call("sudo wget wifipineapple.com/wp6.sh", shell = "True")
        subprocess.call("sudo chmod +x wp6.sh", shell = "True")
        subprocess.call("./wp6.sh", shell = "True")
    elif x == 2:
        subprocess.call("sudo firefox '172.16.42.1:1471'", shell = "True")
    elif x == 3:
        subprocess.call("sudo ssh root@172.16.42.1", shell = "True")
    elif x == 4:
        main()
    else:
         print("Unregonised Input.")
    new_input = input("Press enter to return to pineapple menu or 6 to go back to main menu > ")
    if new_input == "6":
        main()
    else:
        pineapple()

def nmap_menu():
    print_banner()
    print("1. Ping Scan")
    print("2. Standard Service Detection")
    print("3. TCP Syn Scan")
    print("4. Detect Operating System")
    print("5. Detect Operating System and Services")
    print("6. Back")

def nmap():
    nmap_menu()
    x = eval(input(">"))

    if x == 1:
        target = input("Enter Target > ")
        subprocess.call("sudo nmap -sP "+target, shell = "True")
    elif x == 2:
        target = input("Enter Target > ")
        subprocess.call("sudo nmap -sV "+target+" -p 1-65535", shell = "True")
    elif x == 3:
        target = input("Enter Target > ")
        subprocess.call("sudo nmap -sS "+target+" -p 80", shell = "True")
    elif x == 4:
        target = input("Enter Target > ")
        subprocess.call("sudo nmap -O "+target, shell = "True")
    elif x == 5:
        target = input("Enter Target > ")
        subprocess.call("sudo nmap -A "+target, shell = "True")
    elif x == 6:
        main()
    else:
        print("Unregonised Input.")
    new_input = input("Press enter to return to nmap menu or 6 to go back to main menu > ")
    if new_input == "6":
        main()
    else:
        nmap()

def redo_config():
    subprocess.call("sudo python3 ~/Dozy/Code/config.py", shell = "True")

if __name__ == '__main__':
    main()
