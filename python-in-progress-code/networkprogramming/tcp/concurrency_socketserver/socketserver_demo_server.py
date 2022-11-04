import socketserver

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
                data = self.request.recv(1024)
                if not data:
                    break
                # 判断是否是退出信号,是就退出
                if b'exit' == data:
                    self.request.sendall(data)
                    self.request.close()
                    break
                print("接收到客户端%s:%s信息：" % self.client_address, data.decode('utf-8'))
                # 发送信息
                self.request.sendall(data)
            except Exception as e:
                print("Exception", e)
        # self.server.shutdown()


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), TcpSocket_server)
    s.serve_forever()
