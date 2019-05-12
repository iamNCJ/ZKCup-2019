#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
# import threading
import time
import fcntl  # Linux only

is_ready = False
sock = None
addr = []


# def tcplink(sock, addr):
#     global is_ready
#     print('Accept new connection from %s:%s...' % addr)
#     is_ready = True
#     # sock.send(b'Welcome!')
#     while True:
#         data = sock.recv(1024)
#         time.sleep(1)
#         if data == 'exit' or not data:
#             break
#         print(str(data))
#         sock.send(b'Hello, %s!' % data)
#     sock.close()
#     is_ready = False
#     print('Connection from %s:%s closed.' % addr)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def init_socket():
    global sock, addr
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 监听端口:
    ip_address = get_ip_address(b'wifi0')
    s.bind((ip_address, 9998))
    s.listen(5)
    print(ip_address + ':9998')
    print('Waiting for connection...')
    while True:
        # 接受一个新连接:
        sock, addr = s.accept()
        # 创建新线程来处理TCP连接:
        # t = threading.Thread(target=tcplink, args=(sock, addr))
        # t.start()


def get_res():
    if sock:
        sock.send(b'want_res')
        while True:
            data = sock.recv(1024)
            time.sleep(1)
            if data:
                try:
                    msg = data.split()
                    res = int(msg[0])
                    conf = float(msg[1])
                    return [res, conf]
                except:
                    data = None
