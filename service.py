# coding = utf-8

import socket

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(10)
while True:
    c, addr = s.accept()     # 建立客户端连接。
    print('连接地址：', addr)
    print(c.recv(1024).decode('utf-8'))
    c.close()