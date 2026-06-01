# функция проверки корректности вводимых параметров
# в качестве аргумента проверяемое значение и его возможные максимум и минимум int
def _interval(value, minv, maxv):
    return max(minv, min(value, maxv))

print(_interval(-1, 0, 100))

# функция перевода RGB-кода в код для отправки на лампу
# в качестве аргумента значения каналов RGB int
def _rgb_to_code(red, green, blue):
    c_code = (red << 16) | (green << 8) | blue
    return c_code

print(_rgb_to_code(255, 255, 255))