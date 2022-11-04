# import socket
# import os
#
#
# host = ''
# port = 8888
# recv_size = 1024
# upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# upd_server.bind((host, port))
# while True:
#     data, addr = upd_server.recvfrom(1024)
#     cmd = data.decode('utf-8')
#     print('file name:', cmd)
#     file_data = b''
#     if not os.path.exists(cmd):
#         file_data = b''
#     else:
#         with open(cmd,'rb') as f:
#             file_data = f.readlines()
#             for fdt in file_data:
#                 upd_server.sendto(fdt, addr)
#
#     print("response to :", addr)

# udp_server.close()

import socket

count = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 9999)
s.bind(server_addr)

print('Bind UDP on 9999...')
while True:
    if count == 0:
        data, client_addr = s.recvfrom(1024)
        print('connected from %s:%s' % client_addr)
        f = open(data, 'wb')
    data, client_addr = s.recvfrom(1024)
    if str(data) != "b'end'":
        f.write(data)
        print('recieved ' + str(count) + ' byte')
    else:
        break
    s.sendto('ok'.encode('utf-8'), client_addr)
    count += 1
print('recercled' + str(count))
f.close()
s.close()

# data, addr = s.recvfrom(1024)
# print('Received from %s:%s' %addr)
# s.sendto(b'Hello, %s!' %data, addr)
