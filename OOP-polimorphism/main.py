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

host = "134.0.115.28"
port = 22
transport = paramiko.Transport((host,port))

username = "root"
password = "ap4Ainee4uma"
transport.connect(None,username,password)

sftp = paramiko.SFTPClient.from_transport(transport)
#https://stackoverflow.com/questions/3635131/paramikos-sshclient-with-sftp
#Download
filepath = "/etc/passwd"
localpath = "/"
sftp.get(filepath,localpath)



if sftp:
    sftp.close()

if transport:
    transport.close()