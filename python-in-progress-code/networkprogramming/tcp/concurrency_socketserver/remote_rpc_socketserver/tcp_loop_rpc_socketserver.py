import socketserver
import subprocess
import struct

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
                data_cmd = self.request.recv(1024)
                if not data_cmd:
                    break
                # 判断是否是退出信号,是就退出
                if b'exit' == data_cmd:
                    self.request.sendall(data_cmd)
                    self.request.close()
                    break
                print("接收到客户端%s:%s的命令" % self.client_address, data_cmd.decode('utf-8'))
                result = subprocess.Popen(data_cmd.decode('utf-8'), shell=True,
                                          stderr=subprocess.PIPE,
                                          stdout=subprocess.PIPE,
                                          stdin=subprocess.PIPE)
                err = result.stderr.read()  # 通过res.stderr.read()读取错误消息
                if err:
                    res_data = err
                else:
                    res_data = result.stdout.read()  # 通过res.stdout.read()读取标准输出消息
                if not res_data:  # 有些系统命令是没有返回值的，需要处理一下
                    res_data = '执行成功'.encode('gbk')  # 防止操作系统执行命令后，返回值为空时，为客户端返回此消息,这里的编码是gbk因为cmd窗口就是gbk编码的
                _len = len(res_data)
                _len_str = struct.pack('i', _len)
                print("响应客户端的命令。。。。。")
                self.request.sendall(_len_str)
                self.request.sendall(res_data)
            except Exception as e:
                print("Exception", e)
        # self.server.shutdown()


if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8888), TcpSocket_server)
    s.serve_forever()

