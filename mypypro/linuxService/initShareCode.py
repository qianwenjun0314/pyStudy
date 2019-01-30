import os
import paramiko

ssh = paramiko.SSHClient()# ssh.load_host_keys("C:/Users/Administrator/.ssh/known_hosts")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
filename = "shareCode.csv"
localpath = "/Users/qianwenjun/Desktop/" + filename
remotepath = "/root/aiqiyi8/" + filename
server = "116.62.234.69,121.43.161.28,47.97.166.157"
words = server.split(",")
for word in words:
  ssh.connect(word, username = "root", password = "qweQWE123$%^")
  sftp = ssh.open_sftp()
  sftp.put(localpath, remotepath, callback = None)
  ssh.close()
