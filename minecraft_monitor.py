"""
Модуль для мониторинга сервера майнкрафт

Версия: 1.1
Автор: ArtShefer
Дата последнего редактирования: 2022-01-20

Пример использования:

from minecraft_monitor import *
srv = MineMon('localhost', 25565)
print('Подключение: ', srv.Check())
print('Сервер:      ', srv.ip)
print('Порт:        ', srv.port)
print('Статус:      ', srv.status)
print('Motd:        ', srv.motd)
print('Играют:      ', srv.online)
print('Слотов:      ', srv.max)
"""
import socket


class MineMon():
    def __init__(self, server_ip, server_port):
        # Задаем переменные для подключения
        self.ip = server_ip
        self.port = server_port

    def Check(self):
        # Задаем переменные по умолчанию
        self.status = False
        self.motd = None
        self.online = None
        self.max = None

        # Создаем сокет
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Пробуем подключиться
            sock.connect((self.ip, self.port))
        except socket.error:
            # Если не удалось подключиться возвращаем False
            return False
        else:
            # Посылаем пакет
            sock.send(b'\xfe')
            # Принимаем ответ от сервера
            data = sock.recv(2048)
            # Закрываем подключение
            sock.close()

            # Переменная для генерации ответа от сервера
            d = ''
            # Количество первых символов для пропуска
            c = 2

            # Обрабатываем ответ от сервера
            for tmp in data:
                if c < 0:
                    if tmp != 0:
                        # Записываем по одному символу в переменную
                        d += chr(tmp)
                else:
                    c -= 1

            # chr(167) - символ разделитель
            d = d.split(chr(167))

            self.status = True
            self.motd = d[0]
            self.online = d[1]
            self.max = d[2]

            # При успешном выполнении возвращаем True
            return True
