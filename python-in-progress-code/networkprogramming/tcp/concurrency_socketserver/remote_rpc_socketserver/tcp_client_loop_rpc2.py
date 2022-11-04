import socket
import struct

recv_size = 1024
# 创建客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1', 8888))
while True:
    # 发送信息
    cmd = input("请输入命令:")
    if not cmd:
        continue  # 如果输入为空，跳过此次发送
    if 'exit' == cmd:
        break  # 输入exit断开连接
    # 发送命令给服务器
    client.send(cmd.encode("utf-8"))
    # 接收服务器信息
    len_data = client.recv(4)
    header_data = struct.unpack('i', len_data)[0]
    # 获取调用返回数据
    res_len = 0
    res_msg = b''
    while res_len < header_data:
        res_msg += client.recv(recv_size)
        res_len = len(res_msg)
        print(res_len)
    print("执行结果：" + res_msg.decode('gbk'))  # cmd窗口返回的内容是gbk编码的
print("done!")
client.close()
