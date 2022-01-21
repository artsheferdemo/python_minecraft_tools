# Python Minecraft Tools
Набор модулей для взаимодействия с серверами майнкрафт

## minecraft_monitor.py

Получение информации о сервере:

- Motd - описание сервера
- Кол-во игроков онлайн
- Кол-во слотов

Протестировано на:

- ОС: Debian 11, Windows 7, Windows 10
- Python: 3.9.2, 3.8.9

Пример использования:
```python
from minecraft_monitor import *
#from python_minecraft_tools.minecraft_monitor import *
srv = MineMon('localhost', 25565)
print('Connect/Подключение: ', srv.Check())
print('Host/Сервер:         ', srv.ip)
print('Port/Порт:           ', srv.port)
print('Status/Статус:       ', srv.status)
print('Motd:                ', srv.motd)
print('Online/Играют:       ', srv.online)
print('Slots/Слотов:        ', srv.max)
```

## minecraft_client.py
Примечание:

Скрипт не стабильный, не со всех серверов может получить информацию!
Не хватает знаний пофиксить проблему. Я тупой.

Пример использования:
```python
from minecraft_client import *
#from python_minecraft_tools.minecraft_client import *
srv = Client('localhost', 25565)
print('Connect/Подключение: ', srv.Check())
print('Json return:')
if srv.json == None:
    print('No information/Нет информации')
else:
    print(json.dumps(srv.json, indent=4))
```
