from utility import _interval
import colorsys

class RGBTransition(object):
    def __init__(self, red, green, blue, duration=100, brightness=100):
        self.red = red
        self.green = green
        self.blue = blue
        self.duration = duration
        self.brightness = brightness

    def _value(self):
        red = _interval(self.red, 0, 255)
        green = _interval(self.green, 0, 255)
        blue = _interval(self.blue, 0, 255)
        return red * 65536 + green * 256 + blue


class HSVTransition(object):
    def __init__(self, hue, satur, duration=100, brightness=100):
        self.hue = hue
        self.satur = satur
        self.duration = duration
        self.brightness = brightness

    def _value(self):
        hue = _interval(self.hue, 0, 359) / 359
        satur = max(0, min(100, self.satur)) / 100
        red, green, blue = [int(round(col * 255)) for col in colorsys.hsv_to_rgb(hue, satur, 1)]
        return red * 65536 + green * 256 + blue