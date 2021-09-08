import paramiko
from paramiko import SFTPClient
from operator import attrgetter
from pathlib import Path

from paramiko.py3compat import b
# лишние импорты лучше подчищать


class NewSFTP(SFTPClient):
    def listdir_attr(self, path=".", flag=True, ):  # модифицировать метод listdir
        # параметр flag выглядит неочевидно, раз он отвечает за сортировку его бы и назвать соответственно
        # модифицируя что-то для совместимости все добавочные параметры (наш flag) при значении по умолчанию
        # не должны ничего менять, а так вы сразу подменяете результат функции при параметрах по умолчанию
        lst = super().listdir_attr(path)
        if flag:
            # pring излишен, это выглядит как строка для дебага, а наша функция имеет конкертное предназначение
            print('sorted list')
            return sorted(lst, key=attrgetter('st_mtime'))
        else:
            print('List has not been sorted, switch your flag')
            return lst

    def newest(self, path="."):  # метод возвращающий имя самого свежего файла (по дате создания)
        lst = self.listdir_attr(path)
        # вместе с перевым методом, решение выглядит не самым очевидныи образом - явное лучше неявного
        return lst[-1].filename

    def _adjust_cwd(self, path):
        # Здесь накручено что-то лишнее - почему конвертация в bytes? Зачем конвертация в Path? - по заданию мы итак передаем Path
        # получается Path(Path(..)) что не очень логично
        return super()._adjust_cwd(bytes(
            Path(path)))  # возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove


# INFO
# проект конечно тестовый и в приватном репозитории, но персональные данные лучше не публиковать - они не имеют отношения к нашему классу,
# и нужны чисто для тестирования лично вам
host = "134.0.115.28"
username = "root"
password = "ap4Ainee4uma"

# по задаче просилось делать подключение? требовалось поправить класс
# а сейчас если бы я его импортировал в свой модуль у меня выполнится лишний ненужный код
# Connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
sftp = NewSFTP.from_transport(client.get_transport())
