import socket
import os
import struct

host = ''
port = 5555
recv_size = 1024
upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_server.bind((host, port))


def get_file_content_and_len(filename):
    contents = []
    file_len = 0
    with open(filename, 'rb') as f:
        content = f.read(1024)
        while content:
            contents.append(content)
            file_len += len(content)
            content = f.read(1024)
    return file_len, contents


while True:
    data, addr = upd_server.recvfrom(1024)
    cmd = data.decode('utf-8')
    print('file name:', cmd)
    file_data = b''
    if not os.path.exists(cmd):
        # print("no file")
        file_data = b''
    else:
        print("file exists...")
        _len, file_contents = get_file_content_and_len(cmd)
        print(_len)
        # print(file_contents)
        _str_len = struct.pack('i', _len)
        upd_server.sendto(_str_len,addr)
        for c in file_contents:
            print(len(c))
            upd_server.sendto(c,addr)

    print("response to :", addr)

udp_server.close()
