import machine
import network
import json
import sys


# ESP32 Pin assignment 
print('Booting...')        
station = network.WLAN(network.STA_IF)
station.active(True)
rawNetworkInformation = station.scan()
networkNamesInBytes = [i[0].decode() for i in rawNetworkInformation]
try:
    savedNetworks = json.load(open("networks.json","r"))
except Exception as e:
    savedNetworks = {}
for ssid,psswd in savedNetworks.items():
    if ssid in networkNamesInBytes:
        station.connect(ssid,psswd)
        counter = 0
        while station.isconnected() == False and counter < 2000:
            print("Connecting...")
            print(str(counter))
            counter += 1
        if station.isconnected() == True:
            break
        savedNetworks.pop(ssid)
if station.isconnected() == False:
    sys.exit()
else:
    print("IP: ",station.ifconfig()[0])

import urequests
from ubinascii import a2b_base64
class service:
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    
    def getUpdate(self):
        data = urequests.get("http://{}:{}/check-update".format(self.ip,self.port)).json()
        return data['update']
    
    def downloadFiles(self):
        data = urequests.get("http://{}:{}/get_update".format(self.ip,self.port)).json()["files"]
        for filename,d in data.items():
            text = "".join(a2b_base64(d).decode("ascii").split("\r"))
            with open(filename,"w") as file:
                file.write(text)
        machine.reset()
    
    def checkWhetherServerIsOnline(self):
        try:
            data = urequests.get("http://{}:{}".format(self.ip,self.port)).json()
        except Exception as e:
            return False
        return True

with open("config.env","r") as file:
    data = file.readlines()
ip = "".join(data[0].split("\n")).split("=")[-1]
port = data[1].split("=")[-1]
s = service(ip,port)
if s.checkWhetherServerIsOnline() is True:
    if s.getUpdate() == True:
        s.downloadFiles()
        print("Updating")
    print("OTA: Updated")
else:
    print("OTA: Not Updated")

