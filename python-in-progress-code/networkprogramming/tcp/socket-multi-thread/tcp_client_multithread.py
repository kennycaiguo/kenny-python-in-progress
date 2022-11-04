import socket
import threading

recv_size = 1024
# 创建客户端
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1',8000))
while True:
        # 发送信息
        msg = input("请输入发送给服务器的信息:")
        if not msg: continue
        client.send(msg.encode("utf-8"))
        # 接收服务器信息
        data = client.recv(recv_size)
        if b'EXIT' == data:
            break
        print(data.decode('utf-8'))

print("done!")
client.close()
