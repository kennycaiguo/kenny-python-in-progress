import socketserver


class UdpHandler(socketserver.BaseRequestHandler):

    def handle(self) -> None:
        print(self.request)
        # 获取数据
        data = self.request[0]
        if not data:
            return  # 如果信息为空就结束
        upd_srv = self.request[1]
        if b'exit' == data:
            upd_srv.sendto(data, self.client_address)
            return
        print(data.decode("utf-8"))
        upd_srv.sendto(data, self.client_address)


if __name__ == '__main__':
    upd_server = socketserver.ThreadingUDPServer(('127.0.0.1', 6666), UdpHandler)
    upd_server.serve_forever()
