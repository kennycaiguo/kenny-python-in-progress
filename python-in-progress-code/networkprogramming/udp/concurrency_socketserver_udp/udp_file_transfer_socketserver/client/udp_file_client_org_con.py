import socket
import struct

host = '127.0.0.1'
port =6666
recv_size = 1024
addr = (host,port)
upd_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    filename = input("请输入需要下载的文件名>>:")
    if not filename:
        continue
    if 'exit' == filename:
        break
    upd_client.sendto(bytes(filename,'utf-8'),addr)
    _len_str,addr = upd_client.recvfrom(recv_size)
    if b'exit' == _len_str:
        break
    if len(_len_str) == 0:
        print("文件不存在")
        continue
    header_data = struct.unpack('i',_len_str)[0]
    data_len = 0
    f = open(filename,'wb')
    data,addr = upd_client.recvfrom(recv_size)
    data_len = len(data)
    while data_len < header_data:
        f.write(data)
        data,addr = upd_client.recvfrom(recv_size)
        data_len += len(data)
    f.close()
    # data_len = 0
    print("ok!!!")



upd_client.close()
