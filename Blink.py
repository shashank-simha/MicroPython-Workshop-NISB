from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT) # 15 for esp8266

while True:
  led.value(0) # led.low() or led.off()
  sleep(0.5)
  led.value(1) # led.high() or led.on()
  sleep(0.5)