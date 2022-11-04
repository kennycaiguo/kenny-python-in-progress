import socket

recv_size =1024
# 创建服务器
tcp_svr = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定端口
tcp_svr.bind(('127.0.0.1', 8000))
# 监听端口
tcp_svr.listen(1000)
# 接受用户连接,返回连接和对方地址
con,addr = tcp_svr.accept()
# 接收消息
data = con.recv(recv_size)
print(data.decode('utf-8'))
msg = input("请输入发送信息: ")
# 发送信息
con.send(msg.encode('utf-8'))
print("done!!")
con.close()
tcp_svr.close()


