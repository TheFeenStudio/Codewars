import paramiko
from paramiko import SFTPClient
from operator import attrgetter
from pathlib import Path

from paramiko.py3compat import b


class NewSFTP(SFTPClient):
    def listdir_attr(self, path=".", flag=True, ):  # модифицировать метод listdir
        lst = super().listdir_attr(path)
        if flag:
            print('sorted list')
            return sorted(lst, key=attrgetter('st_mtime'))
        else:
            print('List has not been sorted, switch your flag')
            return lst

    def newest(self, path="."):  # метод возвращающий имя самого свежего файла (по дате создания)
        lst = self.listdir_attr(path)
        return lst[-1].filename

    def _adjust_cwd(self, path):
        return super()._adjust_cwd(bytes(
            Path(path)))  # возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove


# INFO
host = "134.0.115.28"
username = "root"
password = "ap4Ainee4uma"

# Connection
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
sftp = NewSFTP.from_transport(client.get_transport())
