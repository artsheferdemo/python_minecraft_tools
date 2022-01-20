# Python Minecraft Tools
Набор модулей для получения информации с серверов майнкрафт

## minecraft_monitor.py

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
