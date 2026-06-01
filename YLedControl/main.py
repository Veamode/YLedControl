import socket
import json

from YLedControl import transition
from YLedControl.comunucation import _sendMessage
from YLedControl.utility import _interval
global settings

# rerf config file



class Lamp(object):
    def __init__(self, ip, port=7777, power='on', timeout=5):
        self.ip = ip
        self.port = port
        self.power = power
        self.timeout = timeout

        self.__cmd_id = 0
        self.__socket = None

        f = open('config.json')  # открывает файл 'config.json', загружает его содержимое в переменную 'conf' в формате словаря (dictionary) при помощи функции 'json.load()', а затем выводит все ключи словаря 'conf' при помощи цикла 'for'.
        self.conf = json.load(open('config.json'))
        f.close()

    # счетчик команд, отправленных на лампу
    def _cmd_id(self):
        self.__cmd_id += 1
        return self.__cmd_id - 1

    def _socket(self):
        if self.__socket is None:
            self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # функция сохраняет текущие настройки как настройки по умолчанию
    def set_default(self):
        with open('settings_list.txt', 'w') as file:
            for line in settings:
                file.write(line + '\n')

        print('Default settings saved to settings_list.txt')
        return _sendMessage('set_default', [])

    # функция получает текущие настройки лампы
    def get_settings(self):
        settings = {}
        with open('settings_list.txt', 'r') as file:
            for line in file:
                settings.update({line})

        print('Settings loaded from settings_list.txt')
        return _sendMessage('get_prop',
                           ['power', 'bright',
                            'ct', 'rgb'])

    # функция изменения яркости
    # в качестве аргумента значение яркости int
    def brightness(self, value):
        hue = _interval(value, 0, 100)
        Lamp.conf.update('brightness', hue)
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))
        return _sendMessage('set_bright', [hue, 500])

    # функция изменения цветовой температуры
    # в качестве аргумента значение цветовой температуры int
    def temperature(self, value):
        hue = _interval(value, 1700, 6500)
        Lamp.conf.update('brightness', hue)
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))
        return _sendMessage('set_ct_abx', [hue, 500])