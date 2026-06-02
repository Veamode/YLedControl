import YLedControl
import time

lamp = YLedControl.Lamp('192.168.1.104')

# включение лампы
lamp.power_on()

# получение текущих параметров
lamp.get_settings()
time.sleep(2)

# изменение режима работы
lamp.power_switch()
time.sleep(2)
lamp.power_switch()
time.sleep(2)

# изменение яркости
lamp.brightness(10)
time.sleep(2)
lamp.brightness(100)
time.sleep(2)

# изменение цветовой температуры
lamp.temperature(1700)
time.sleep(2)
lamp.temperature(6500)
time.sleep(2)

# установка цвета
lamp.set_rgb('255.0.0')
time.sleep(2)
lamp.set_rgb('orange')
time.sleep(2)
lamp.set_hsv('90.100.100')
time.sleep(2)
lamp.set_hsv('white')
time.sleep(2)

# сохранение текущих настроек, как настройки по умолчанию
lamp.set_default()

# выключение лампы
lamp.power_off()

