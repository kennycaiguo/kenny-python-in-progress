import socket
import socketserver
import subprocess


# host = ''
# port = 8888
# recv_size = 1024
# upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# upd_server.bind((host, port))
class UdpHandle(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        udp_srv = self.request[1]

        data = self.request[0]
        if not data: return
        if b'exit' == data:
            udp_srv.sendto(data, self.client_address)
        cmd = data.decode('utf-8')
        print('收到客户端命令', cmd)
        res = subprocess.Popen(cmd, shell=True,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        err = res.stderr.read()
        if err:
            res_data = err
        else:
            res_data = res.stdout.read()
        if not res_data:
            res_data = "command executed successfully.....".encode('gbk')
        udp_srv.sendto(res_data, self.client_address)
        print("response to :", self.client_address)


if __name__ == '__main__':
    udp = socketserver.ThreadingUDPServer(('127.0.0.1', 7777), UdpHandle)
    udp.serve_forever()
