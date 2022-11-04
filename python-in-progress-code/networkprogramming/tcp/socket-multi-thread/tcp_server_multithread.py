import socket
import threading

recv_size = 1024
# 创建服务器
tcp_svr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
tcp_svr.bind(('127.0.0.1', 8000))
# 监听端口
tcp_svr.listen(1000)


def _server(conn):
    while True:
        data = conn.recv(recv_size)
        if not data: break
        print(data.decode('utf-8'))
        conn.send(data.upper())


if __name__ == '__main__':
    while True:
        conn, addr = tcp_svr.accept()
        print("创建新会话")
        s = threading.Thread(target=_server,args=(conn,))
        s.start()
# while True:  # 保证服务器可以在一个客户端关闭后仍然可以和别的客户端通讯
#     print("开始新会话。。。")
#     # 接受用户连接,返回连接和对方地址
#     con,addr = tcp_svr.accept()
#     while True:
#         try:
#             # 接收消息
#             data = con.recv(recv_size)
#             if not data:  # 这个在Linux系统下面需要写，在windows系统下面可以不写
#                 break
#             if data.decode('utf-8') == 'q':
#                 con.send('q'.encode('utf-8'))
#                 break
#             print(data.decode('utf-8'))
#             msg = input("请输入发送信息: ")
#             # 发送信息
#             con.send(msg.encode('utf-8'))
#         except Exception as e:
#             print('程序异常：',e)
#
#     print("done!!")
#     con.close()

tcp_svr.close()
