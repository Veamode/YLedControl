import socket
from asyncio import timeout

# import ifaddr
import json
import requests
# from .main import Lamp



# /// summary
# ///gtrgvtggv tbhtrb
# /// param

# функция отправки команды на лампу
# в качестве аргумента название команды str и массив с параметрами
def _sendMessage(lamp: object, method: str, params: list):
    command = {
        'id': 1,
        'method': method,
        'params': params
    }

    message = json.dumps(command) + '\r\n'

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(lamp.timeout)

            sock.connect((lamp.ip, lamp.port))
            sock.sendall(message.encode('utf-8'))

            response = sock.recv(1024).decode('utf-8')

            if not response:
                raise Exception('Лампа не вернула ответ на команду')

            return response

    except socket.timeout:
        raise Exception('Превышено время ожидания ответа от лампы')

    except ConnectionRefusedError:
        raise Exception('Не подключено. Проверьте, включена ли лампа и доступна ли она в сети')

    except OSError:
        raise Exception('Ошибка сетевого подключения')

    except json.JSONDecodeError:
        raise Exception('Ошибка обработки ответа устройства')

    except EOFError:
        raise Exception('Неизвестная ошибка')

#   def get_ip(name):
#       for ad in ifaddr.get_adapters():
#           if ad.name != name:
#               continue
#           for ip in ad.ips:
#               if not isinstance(ip.ip, tuple):
#                   return ip.ip
#       return None

#   def send_pack(timeout=2, interface=False, ip_ad=''):
#       pass

    # f = open('config.json')
    # conf = json.load(open('config.json'))
    # f.close()
    #
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.settimeout(Lamp.timeout)
    #     s.connect(Lamp.ip, Lamp.port)
    #
    #     response = s.recv(1024)
    #     return response



    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  # заголовки запроса
    # response = requests.post(url, json=json_data, headers=headers)  # отправка POST запроса
    #
    # # обрабатываем ответ и выводим его в поле вывода
    # if response.status_code == 200:
    #     print('отправлено')
    #     # form.textEdit.append('О, все прошло успешно!\n')  # выводим значение в line_edit
    # else:
    #     print('не отправлено')
    #     # form.textEdit.append('Ошибка при получении данных')
