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
        # можно же было просто свой же метод вызвать с флагом
        # return self.listdir_attr(path, True)[-1].filename  # реализацию незачем дублировать
        lst = self.listdir_attr(path, sort=True)
        return lst[-1].filename

    def _adjust_cwd(self, path):
        return super()._adjust_cwd(str(path))  # возможность передавать объект Path из pathlib в качестве пути в методах get, put, remove
