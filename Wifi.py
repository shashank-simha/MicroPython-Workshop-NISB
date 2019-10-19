import network
from time import sleep

def connect():
    ssid = "Redmi Y1"
    password =  "123454321"
 
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return station.ifconfig()
        
    station.active(True)
    station.connect(ssid, password)
    
    for i in range(10):
        if(station.isconnected() == True):
            print("Connection successful")
            print(station.ifconfig())
            break
        print("Retrying.........("+str(i+1)+")")
        sleep(1)
        
    if(station.isconnected() == True):
        return station.ifconfig()
    else:
        return False
