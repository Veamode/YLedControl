import json

from .comunucation import _sendMessage
from .main import Lamp

# функция включения лампы
# def power_on():
#     print('Power on')
#     Lamp.conf.update('power', ['on'])
#     with open('config.json', 'w') as outfile:
#         outfile.write(json.dumps(Lamp.conf))
#     return _sendMessage('set_power', ['on', 500])

# функция выключения лампы
# def power_off():
#     print('Power off')
#     Lamp.conf.update('power', ['off'])
#     with open('config.json', 'w') as outfile:
#         outfile.write(json.dumps(Lamp.conf))
#     return _sendMessage('set_power', ['off', 500])
#
# # функция изменения состояния лампы
# def power_switch():
#     print('Power switch')
#     return _sendMessage('toggle', [])

