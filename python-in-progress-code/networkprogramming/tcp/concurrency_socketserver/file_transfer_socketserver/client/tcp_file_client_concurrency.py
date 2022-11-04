import os
import socket
import struct

recv_size = 1024
# 创建客户端
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器
client.connect(('127.0.0.1', 8888))
while True:
    # 发送信息
    cmd = input("文件名:").strip()  # strip()方法去除空格
    if not cmd:
        continue  # 如果输入为空，跳过此次发送
    if 'exit' == cmd:
        break  # 输入exit断开连接
    # 发送命令给服务器
    client.send(cmd.encode("utf-8"))
    # 接收服务器信息
    len_data = client.recv(4)
    header_data = struct.unpack('i', len_data)[0]
    if header_data == 0:  # 返回空字符串上面文件不存在，跳过本次循环
        print("文件不存在。。。")
        continue
    else:
        # 获取调用返回数据
        res_len = 0
        res_msg = b''
        with open(cmd,'wb') as f:
            while res_len < header_data:
                res_msg = client.recv(recv_size)
                res_len += len(res_msg)
                # print(res_len)
                f.write(res_msg)
            print('file saved...')

print("done!")
client.close()
