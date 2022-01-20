"""
Модуль для мониторинга сервера майнкрафт
Информация которую может получить клиент игры

Version: 1.0
Autor: Prozorovskiy Sergey (ArtShefer)
Data update: 2022-01-20

Example/Пример использования:

from minecraft_client import *
#from python_minecraft_tools.minecraft_client import *
srv = Client('localhost', 25565)
print('Connect/Подключение: ', srv.Check())
print('Json return:')
if srv.json == None:
    print('No information/Нет информации')
else:
    print(json.dumps(srv.json, indent=4))
"""
import socket
import json


class Client():
    def __init__(self, server_ip, server_port):
        self.ip = server_ip
        self.port = server_port

    def Check(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.json = None

        try:
            sock.connect((self.ip, self.port))
        except socket.error:
            return False
        else:
            sock.send(b'\x14\x00\xf2\x05\x0d' + self.ip.encode('utf-8') +  b'\x63\xdd\x01\x01\x00')
            data = sock.recv(8192) #8192
            sock.close()

            d = ''
            c = 4

            for tmp in data:
                if c < 0:
                    if tmp != 0:
                        d += chr(tmp)
                else:
                    c -= 1

            data_json = json.loads(d)
            self.json = data_json

            return True
