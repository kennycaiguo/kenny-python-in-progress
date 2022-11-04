import socket
import time

host = ''
port = 6666
recv_size = 1024
upd_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
upd_server.bind((host, port))
while True:
    data, addr = upd_server.recvfrom(1024)
    # 给客户端返回他指定的格式化时间
    if not data:   # 判断是否是用户没有输入或者是空字符串
        time_fmt = '%Y-%m-%d %X'
    elif data.decode('utf-8') == '' or data.decode('utf-8') == "":
        time_fmt = '%Y-%m-%d %X'
    else:
        time_fmt = data.decode('utf-8')
    data = time.strftime(time_fmt)
    print(data)
    s_data = "格式化后的时间:" + data
    upd_server.sendto(s_data.encode('utf-8'), addr)
    print("response to :", addr)

udp_server.close()
