import socket
import os
import struct

recv_size = 1024
# 创建服务器
tcp_svr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_svr.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) # #加入这条socket配置，重用IP和端口，还可以在操作系统上配置ip和端口重用
# 绑定端口
tcp_svr.bind(('127.0.0.1', 8000))
# 监听端口
tcp_svr.listen(1000)
while True:  # 保证服务器可以在一个客户端关闭后仍然可以和别的客户端通讯
    print("开始新会话。。。")
    # 接受用户连接,返回连接和对方地址
    con,addr = tcp_svr.accept()
    print(addr)
    while True:
        try:
            # 接收消息
            file_name = con.recv(recv_size)
            print(file_name.decode('utf-8'))
            if not file_name:  # 这个在Linux系统下面需要写，在windows系统下面可以不写
                break
            file_data = b''
            if not os.path.exists(file_name):
                file_data = ''
            else:
                with open(file_name,'rb') as f:
                    file_data = f.read()
            _len = len(file_data)
            _len_str = struct.pack('i',_len)
            con.send(_len_str)
            con.send(file_data)
        except Exception as e:
            print('程序异常：',e)

    print("done!!")
    con.close()

tcp_svr.close()


