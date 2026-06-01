from YLedControl.comunucation import _sendMessage
from YLedControl.utility import _interval, _rgb_to_code
from main import Lamp
import json


# функция обработки RGB-кода и названия цвета
# в качестве аргумента RGB-код или название цвета str
def set_rgb(n_color):
    print('Setting RGB color')
    if n_color[0] in '0123456789':
        res = []
        c = n_color.split('.')
        for i in c:
            hue = _interval(i, 0, 255)
            res.append(hue)

        Lamp.conf.update('color', res)
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))

        hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
        return _sendMessage('set_rgb', [hue, 500])


    else:
        if n_color[0] == 'red':
            res = ['255', '0', '0']
        elif n_color[0] == 'orange':
            res = ['255', '110', '0']
        elif n_color[0] == 'yellow':
            res = ['255', '255', '0']
        elif n_color[0] == 'green':
            res = ['0', '255', '0']
        elif n_color[0] == 'blue':
            res = ['0', '0', '255']
        elif n_color[0] == 'pink':
            res = ['255', '192', '203']
        else:
            res = ['255', '255', '255']

        Lamp.conf.update('color', res)
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))

        hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
        return _sendMessage('set_rgb', [hue, 500])

# функция обработки HSV-кода и названия цвета
# в качестве аргумента HSV-код или название цвета str
def set_hsv(n_color):
    print('Setting HSV color')
    if n_color[0] in '0123456789':
        color = n_color.split('.')

        h = _interval(int(color[0]), 0, 360)
        s = _interval(int(color[1]), 0, 100)
        v = _interval(int(color[2]), 0, 100)
        c = int(v) * int(s)
        x = int(c) * (1 - abs((int(h) / 60) % 2 -1))
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
        Lamp.conf.update('color', [r, g, b])
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))

        hue = _rgb_to_code(r, g, b)
        return _sendMessage('set_rgb', [hue, 500])


    else:
        if n_color[0] == 'red':
            res = ['255', '0', '0']
        elif n_color[0] == 'orange':
            res = ['255', '110', '0']
        elif n_color[0] == 'yellow':
            res = ['255', '255', '0']
        elif n_color[0] == 'green':
            res = ['0', '255', '0']
        elif n_color[0] == 'blue':
            res = ['0', '0', '255']
        elif n_color[0] == 'pink':
            res = ['255', '192', '203']
        else:
            res = ['255', '255', '255']

        Lamp.conf.update('color', res)
        with open('config.json', 'w') as outfile:
            outfile.write(json.dumps(Lamp.conf))

        hue = _rgb_to_code(int(res[0]), int(res[1]), int(res[2]))
        return _sendMessage('set_rgb', [hue, 500])

        # if n_color[0] == 'red':
        #     return 'color', ['0', '100', '100']
        # elif n_color[0] == 'orange':
        #     return 'color', ['39', '100', '100']
        # elif n_color[0] == 'yellow':
        #     return 'color', ['60', '100', '100']
        # elif n_color[0] == 'green':
        #     return 'color', ['120', '100', '100']
        # elif n_color[0] == 'blue':
        #     return 'color', ['240', '100', '100']
        # elif n_color[0] == 'pink':
        #     return 'color', ['350', '10', '100']
        # else:
        #     return 'color', ['0', '0', '100']
