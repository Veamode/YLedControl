import socket
import json


# счетчик команд, отправленных на лампу
def _cmd_id(lamp: object):
    lamp.__cmd_id += 1
    return lamp.__cmd_id - 1

# функция отправки команды на лампу
# в качестве аргумента название команды str и массив с параметрами
def _sendMessage(lamp: object, method: str, params: list):
    command = {
        'id': _cmd_id(lamp),
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
            print(response)

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