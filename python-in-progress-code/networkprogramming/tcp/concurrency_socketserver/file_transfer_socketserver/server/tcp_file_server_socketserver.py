import socketserver
import struct
import os
"""
socketserver可以实现并发
利用socketserver编程需要自己定义一个类继承socketserver.BaseRequestHandler

"""


class TcpSocket_server(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        print("connection:", self.request)
        # print("address:", self.client_address)

        # 通信
        while True:
            try:
                file_name = self.request.recv(1024)
                if not file_name:
                    break
                # 判断是否是退出信号,是就退出
                if b'exit' == file_name:
                    self.request.sendall(file_name)
                    self.request.close()
                    break
                print("filename:", file_name.decode('utf-8'))
                # 发送文件
                file_data = b''
                if not os.path.exists(file_name):
                    file_data = ''
                else:
                    with open(file_name, 'rb') as f:
                        file_data = f.read()
                _len = len(file_data)
                _len_str = struct.pack('i', _len)
                self.request.sendall(_len_str)
                self.request.sendall(file_data)
            except Exception as e:
                print("Exception", e)
        # self.server.shutdown()


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), TcpSocket_server)
    s.serve_forever()
