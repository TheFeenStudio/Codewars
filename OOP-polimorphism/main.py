import paramiko
from paramiko import SFTPClient
from pathlib import PurePath

class NewSFTP(SFTPClient):
    def put(self, localpath, remotepath, callback=None, confirm=True):
        super().put(self, PurePath, remotepath, callback=None, confirm=True)

    def get(self, remotepath, localpath, callback=None):
        super().get(self, remotepath, PurePath, callback=None)

    def remove(self, path):
        super().remove(self, PurePath)


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
client.connect(hostname='134.0.115.28', username='root', password='ap4Ainee4uma', allow_agent=False, look_for_keys=False)

sftp = client.open_sftp()
sftp.put('text.txt', 'uploaded.txt')
sftp.close()