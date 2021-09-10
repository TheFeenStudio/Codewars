from paramiko import SFTPClient
from operator import attrgetter
from pathlib import Path
import paramiko

# На основе класса SFTPClient библиотеки paramiko создать собственный класс, который реализует:
#
# возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove (и прочие методы которые принимают путь)
# метод возвращающий имя самого свежего файла (по дате создания)
# модифицировать метод listdir (и listdir_attr), добавив флаг сортировки (только по дате создания)


class NewSFTP(SFTPClient):
    def listdir_attr(self, path=".", sort=False):  # модифицировать метод listdir
        lst = super().listdir_attr(path)
        if sort:
            return sorted(lst, key=attrgetter('st_mtime'))
        else:
            return lst

    def newest(self, path="."):  # метод возвращающий имя самого свежего файла (по дате создания)
        lst = self.listdir_attr(path, sort=True)
        return lst[-1].filename

    def _adjust_cwd(self, path):
        return super()._adjust_cwd(str(path))  # возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove

#INFO
host = ''
username = ''
password = ''

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
sftp = NewSFTP.from_transport(client.get_transport())
