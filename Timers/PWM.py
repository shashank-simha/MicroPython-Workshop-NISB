from machine import Pin, PWM

fade = PWM(Pin(2)) # 15 for esp8266      
fade.freq(1000)                     
fade.duty((50/100)*1024)         

# fade = PWM(Pin(2), freq=500, duty=(50/100)*1024)

fade.deinit()           
