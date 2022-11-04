# import socket
#
# host = '127.0.0.1'
# port = 8888
# recv_size = 1024
# addr = (host,port)
# upd_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# while True:
#     filename = input("请输入需要下载的文件名>>:")
#     if not filename:
#         continue
#     if 'exit' == filename:
#         break
#     upd_client.sendto(bytes(filename,'utf-8'),addr)
#     data,addr = upd_client.recvfrom(recv_size)
#     if len(data) == 0:
#         print('文件不存在')
#     else:
#         with open(filename,'wb') as f:
#             if not data:
#                 break
#             f.write(data)

import socket
import os
import time


def Get_FilePath_FileName_FileExt(filename):
    filepath, tempfilename = os.path.split(filename)
    shotname, extension = os.path.splitext(tempfilename)
    return filepath, shotname, extension


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input('please enter the filename you want to send:\n')
filepath, shotname, extension = Get_FilePath_FileName_FileExt(filename)

client_addr = ('127.0.0.1', 9999)
f = open(filename, 'rb')
count = 0
flag = 1
while True:
    if count == 0:
        data = bytes(shotname + extension, encoding="utf8")
        start = time.time()
        s.sendto(data, client_addr)
    data = f.read(1024)
    if str(data) != "b''":
        s.sendto(data, client_addr)
        print(str(count) + 'byte')

    else:
        s.sendto('end'.encode('utf-8'), client_addr)
        break
    data, server_addr = s.recvfrom(1024)
    count += 1
print('recircled' + str(count))
s.close
end = time.time()
print('cost' + str(round(end - start, 2)) + 's')
# for data in [b'Michael',b'Tracy',b'Sarah']:
#  s.sendto(data,('127.0.0.1',9999))
#  print(s.recv(1024).decode('utf-8'))
# s.close()
