import os
import paramiko

ssh = paramiko.SSHClient()  # ssh.load_host_keys("C:/Users/Administrator/.ssh/known_hosts")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
filename = "genUid.py"
localpath = "/Users/qianwenjun/work/CODE/myPyPro/pythonStudy/mypypro/demo/" + filename
remotepath = "/root/test/" + filename
server = "47.105.193.249"
words = server.split(",")
for word in words:
  ssh.connect(word, username="root", password="930314qwjA")
  sftp = ssh.open_sftp()
  sftp.put(localpath, remotepath, callback = None)
  ssh.close()
