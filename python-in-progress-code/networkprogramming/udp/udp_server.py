import socket
from time import ctime

host = ''
port = 8888
recv_size = 1024
upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_server.bind((host,port))
while True:
    data, addr = upd_server.recvfrom(1024)
    upd_server.sendto(bytes('[%s]%s'%(ctime(),data.decode('utf-8')),'utf-8'),addr)
    print("response to :",addr)

udp_server.close()

