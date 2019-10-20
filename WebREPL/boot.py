import network
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='MyESP8266', authmode=network.AUTH_WPA_WPA2_PSK, password='mypassword')
print(ap.config('essid'))

import webrepl_setup
import webrepl
webrepl.start()