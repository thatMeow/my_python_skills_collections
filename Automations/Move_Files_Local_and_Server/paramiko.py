import paramiko

transfer_from = r'path/file' # local machine
transfer_to = r'/server_path/file'
hostname = 'linux.server.com'
port = 22 # default port for SSH
username = 'user'
password = 'secret'

try:
    t = paramiko.Transport((hostname, port))
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(transfer_from, transfer_to)
finally:
    t.close()
