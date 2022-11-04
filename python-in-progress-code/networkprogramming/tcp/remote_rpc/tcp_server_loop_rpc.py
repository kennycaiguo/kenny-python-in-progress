import socket
import subprocess
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
    while True:
        try:
            # 接收消息
            data_cmd = con.recv(recv_size)
            if not data_cmd:  # 这个在Linux系统下面需要写，在windows系统下面可以不写
                break
            # print(data_cmd.decode('utf-8'))
            # 执行命令，shell=True,表示指令为字符串，False表示指令为序列
            # subprocess.PIPE返回一个文件展示给用户看
            result = subprocess.Popen(data_cmd.decode('utf-8'),shell=True,
                                      stderr=subprocess.PIPE,
                                      stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE)
            err = result.stderr.read() # 通过res.stderr.read()读取错误消息
            if err:
                res_data = err
            else:
                res_data = result.stdout.read()  # 通过res.stdout.read()读取标准输出消息
            if not res_data:  # 有些系统命令是没有返回值的，需要处理一下
                res_data = '执行成功'.encode('gbk')  # 防止操作系统执行命令后，返回值为空时，为客户端返回此消息,这里的编码是gbk因为cmd窗口就是gbk编码的
            _len = len(res_data)
            _len_str = struct.pack('i',_len)
            con.send(_len_str)
            con.send(res_data)
        except Exception as e:
            print('程序异常：',e)

    print("done!!")
    con.close()

tcp_svr.close()


