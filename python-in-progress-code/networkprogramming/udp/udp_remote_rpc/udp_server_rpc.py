import socket
import subprocess

host = ''
port = 8888
recv_size = 1024
upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_server.bind((host, port))
while True:
    data, addr = upd_server.recvfrom(1024)
    cmd = data.decode('utf-8')
    print('收到客户端命令', cmd)
    res = subprocess.Popen(cmd, shell=True,
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    err = res.stderr.read()
    if err:
        res_data = err
    else:
        res_data = res.stdout.read()
    if not res_data:
        res_data = "command executed successfully.....".encode('gbk')
    upd_server.sendto(res_data,addr)
    print("response to :", addr)

udp_server.close()
