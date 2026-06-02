import socket
import json

from .comunucation import _sendMessage
from .utility import _interval, _rgb_to_code


class Lamp(object):
    def __init__(self, ip, port=55443, power='on', timeout=5):
        self.ip = ip
        self.port = port
        self.power = power
        self.timeout = timeout

        self.__cmd_id = 0
        self.__socket = None


    def _socket(self):
        if self.__socket is None:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # функция сохраняет текущие настройки, как настройки по умолчанию
    def set_default(self):
        return _sendMessage(self, 'set_default', [])

    # функция получает текущие настройки лампы
    def get_settings(self):
        return _sendMessage(self, 'get_prop',
                           ['power', 'bright',
                            'ct', 'rgb'])

    # функция изменения яркости
    # в качестве аргумента значение яркости int
    def brightness(self, value):
        hue = _interval(value, 0, 100)
        return _sendMessage(self, 'set_bright', [hue, 500, 1])

    # функция изменения цветовой температуры
    # в качестве аргумента значение цветовой температуры int
    def temperature(self, value):
        hue = _interval(value, 1700, 6500)
        return _sendMessage(self, 'set_ct_abx', [hue, 500, 1])

    # функция включения лампы
    def power_on(self):
        print('Power on')
        return _sendMessage(self, 'set_power', ['on', 500, 1])

    # функция выключения лампы
    def power_off(self):
        print('Power off')
        return _sendMessage(self, 'set_power', ['off', 500, 1])

    # функция изменения состояния лампы
    def power_switch(self):
        print('Power switch')
        return _sendMessage(self, 'toggle', [])

    # функция обработки RGB-кода и названия цвета
    # в качестве аргумента RGB-код или название цвета str
    def set_rgb(self, n_color):
        print('Setting RGB color')
        if n_color[0] in '0123456789':
            res = []
            c = n_color.split('.')
            for i in c:
                hue = _interval(int(i), 0, 255)
                res.append(hue)

            hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
            return _sendMessage(self, 'set_rgb', [hue, 500, 1])

        else:
            if n_color == 'red':
                res = ['255', '0', '0']
            elif n_color == 'orange':
                res = ['255', '110', '0']
            elif n_color == 'yellow':
                res = ['255', '255', '0']
            elif n_color == 'green':
                res = ['0', '255', '0']
            elif n_color == 'blue':
                res = ['0', '0', '255']
            elif n_color == 'pink':
                res = ['255', '192', '203']
            elif n_color == 'white':
                res = ['255', '255', '255']
            else:
                res = ['255', '255', '255']

            hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
            return _sendMessage(self, 'set_rgb', [hue, 500, 1])

    # функция обработки HSV-кода и названия цвета
    # в качестве аргумента HSV-код или название цвета str
    def set_hsv(self, n_color):
        print('Setting HSV color')
        if n_color[0] in '0123456789':
            color = n_color.split('.')

            h = _interval(int(color[0]), 0, 360)
            s = _interval(int(color[1]), 0, 100)
            v = _interval(int(color[2]), 0, 100)
            c = int(v) * int(s)
            x = int(c) * (1 - abs((int(h) / 60) % 2 - 1))
            m = int(v) - int(c)
            if 0 <= h < 60:
                r1, g1, b1 = c, x, 0
            elif 60 <= h < 120:
                r1, g1, b1 = x, c, 0
            elif 120 <= h < 180:
                r1, g1, b1 = 0, c, x
            elif 180 <= h < 240:
                r1, g1, b1 = 0, x, c
            elif 240 <= h < 300:
                r1, g1, b1 = x, 0, c
            elif 300 <= h < 360:
                r1, g1, b1 = c, 0, x
            else:
                raise ValueError("h должно быть в диапазоне от 0 до 360")
            r = round((r1 + m) * 255)
            g = round((g1 + m) * 255)
            b = round((b1 + m) * 255)

            hue = _rgb_to_code(r, g, b)
            return _sendMessage(self, 'set_rgb', [hue, 500, 1])

        else:
            if n_color == 'red':
                res = ['255', '0', '0']
            elif n_color == 'orange':
                res = ['255', '110', '0']
            elif n_color == 'yellow':
                res = ['255', '255', '0']
            elif n_color == 'green':
                res = ['0', '255', '0']
            elif n_color == 'blue':
                res = ['0', '0', '255']
            elif n_color == 'pink':
                res = ['255', '192', '203']
            elif n_color == 'white':
                res = ['255', '255', '255']
            else:
                res = ['255', '255', '255']

            hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
            return _sendMessage(self, 'set_rgb', [hue, 500, 1])