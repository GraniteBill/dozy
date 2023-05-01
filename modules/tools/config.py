import configparser

wlan_interface = input('Enter wireless interface: ')
eth_interface = input('Enter ethernet interface: ')
config = configparser.ConfigParser()
config.read('../Config/config.ini')
config['DEFAULT']['wlan_interface'] = wlan_interface
config['DEFAULT']['eth_interface'] = eth_interface
config['DEFAULT']['bssid'] = 'N/A'
config['DEFAULT']['channel'] = 'N/A'
config['DEFAULT']['essid'] = 'N/A'
config['DEFAULT']['scan'] = '0'
config['DEFAULT']['cipher'] = 'N/A'
config['DEFAULT']["wps"] = 'N/A'
with open('../Config/config.ini', 'w') as configfile:
    config.write(configfile)
