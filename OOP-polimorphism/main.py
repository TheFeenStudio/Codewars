import paramiko
from paramiko import SFTPClient
from operator import attrgetter
from pathlib import Path


class NewSFTP(SFTPClient):
    def listdir_attr(self, path=".", flag=True, ):  # модифицировать метод listdir
        lst = super().listdir_attr(path)
        if flag:
            print('sorted list')
            return sorted(lst, key=attrgetter('st_mtime'))
        else:
            return lst


    def newest(self, path="."):  # метод возвращающий имя самого свежего файла (по дате создания)
        lst = self.listdir_attr(path)
        print(lst[-1].filename)


    def get(self, remotepath, localpath, callback=None):
        get = super().get(remotepath, localpath, callback=None)
        print(get)


# INFO
host = "134.0.115.28"
username = "root"
password = "ap4Ainee4uma"

# Connect
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False)
sftp = SFTPClient.from_transport(client.get_transport())
# list = sftp.listdir_attr(flag=True)
newest = sftp.get('/Users/maxim/desktop',)
