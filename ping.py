from http import server
import os
import subprocess
import json

from cairo import Status

count = 1

ip_list = {'TrueNas': ['10.10.10.10', 'DOWN'],
           'Desktop': ['10.10.10.9', 'DOWN'],
           'Torrent-box': ['10.10.10.206', 'DOWN'],
           'Plex': ['10.10.10.43', 'DOWN'],
           'HomeAssistant': ['10.10.10.7', 'DOWN'],
           'InfluxDB': ['10.10.10.13', 'DOWN'],
           'Portainer': ['10.10.10.8', 'DOWN'],
           'PiHole': ['10.10.10.2', 'DOWN'],
           'Mikrotik': ['10.10.10.3', 'DOWN']}

for key, item in ip_list.items():
    response = os.popen(f"ping -c {count} -W 3 {item[0]}").read()
    if f"{count} received" in response:
        ip_list[key][1] = 'UP'
    else:
        ip_list[key][1] = 'DOWN'

with open('convert.txt', 'w') as convert_file:
    convert_file.write(json.dumps(ip_list))
