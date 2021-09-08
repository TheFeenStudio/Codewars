from paramiko import SFTPClient
from operator import attrgetter
from pathlib import Path


class NewSFTP(SFTPClient):
    def listdir_attr(self, path=".", sort=False):  # модифицировать метод listdir
        lst = super().listdir_attr(path)
        if sort:
            return sorted(lst, key=attrgetter('st_mtime'))
        else:
            return lst

    def newest(self, path="."):  # метод возвращающий имя самого свежего файла (по дате создания)
        lst = super().listdir_attr(path)
        lst = sorted(lst, key=attrgetter('st_mtime'))
        return lst[-1].filename

    def _adjust_cwd(self, path):
        p = Path(path)
        return super()._adjust_cwd(str(p))  # возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove
