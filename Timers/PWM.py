from machine import Pin, PWM

fade = PWM(Pin(2)) # 15 for esp8266      
fade.freq(1000)
                    
while True:
    for i in range(10):
        fade.duty((i/10)*1024)
        delay_ms(100)
    for i in range(10):
        fade.duty(((10-i)/10)*1024)
        delay_ms(100)

# fade = PWM(Pin(2), freq=500, duty=(50/100)*1024)

#fade.deinit()           
