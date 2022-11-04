import socketserver
import os
import struct


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


class UdpHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:

        # 获取数据
        data = self.request[0]
        if not data:
            return  # 如果信息为空就结束
        upd_srv = self.request[1]
        if b'exit' == data:
            upd_srv.sendto(data, self.client_address)
            return
        cmd = data.decode('utf-8')
        print('file name:', cmd)
        if not os.path.exists(cmd):
            file_contents = b''
            upd_srv.sendto(file_contents, self.client_address)
        else:
            print("file exists...")
            _len, file_contents = get_file_content_and_len(cmd)
            # print(_len)
            # print(os.path.getsize(cmd))
            # print(file_contents)
            _str_len = struct.pack('i', _len)
            # print(_str_len)
            upd_srv.sendto(_str_len, self.client_address)
            for c in file_contents:
                upd_srv.sendto(c, self.client_address)

        print("response to :", self.client_address)


if __name__ == '__main__':
    upd_server = socketserver.ThreadingUDPServer(('127.0.0.1', 6666), UdpHandler)
    upd_server.serve_forever()
