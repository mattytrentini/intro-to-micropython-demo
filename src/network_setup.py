import network

import random

ssid = "MPDemo" + str(random.randint(1000, 9999))
password = "mppassword"

ap = network.WLAN(network.AP_IF)
ap.active(False)
ap.config(essid=ssid, password=password) #, authmode=network.AUTH_WPA2_PSK)
ap.active(True)

while not ap.active():
    pass

print(f"Network '{ssid}' setup successfully")
print(ap.ifconfig())