from YLedControl import *
import time

lamp = connect('192.168.1.1')

lamp.power_on()

state = lamp.get_settings()
print(state)

for i in range(3):
    lamp.power_on()
    time.sleep(0.5)
    lamp.power_off()
    time.sleep(0.5)

lamp.set_rgb('255.0.0')
time.sleep(1)
lamp.set_rgb('blue')
time.sleep(1)
lamp.set_hsv('90.100.100')
time.sleep(1)
lamp.set_hsv('yellow')

lamp = Lamp("192.168.1.5")

lamp.power_on()
lamp.power_off()

lamp.brightness(100)

lamp.power_off()

