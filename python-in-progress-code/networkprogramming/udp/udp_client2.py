import socket

host = '127.0.0.1'
port = 8888
recv_size = 1024
addr = (host,port)
upd_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = input("请输入信息>>:")
    if not msg:
        break
    upd_client.sendto(bytes(msg,'utf-8'),addr)
    data,addr = upd_client.recvfrom(recv_size)
    if not data:
        break
    print(data.decode('utf-8'))
upd_client.close()
