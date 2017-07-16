# client class
# -*- coding: utf-8 -*-

import os
import sys
import socket
import select
import time
from ProcessSupport import *

DEFAULT_PORT = 8888
socket_list  = []
TIME_OUT     = 2
RECV_BUFFER  = 4096

# bind a socket
def connect_to_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIME_OUT)
    except BaseException as e:
        print "Error", e
        return False
    else:
        return s

def try_to_server(s, host):
    try:
        s.connect((host, DEFAULT_PORT))
    except BaseException as e:
        print "Error", e
        return False
    else:
        return True

def stream_data(sock, s):
    if sock == s:
        # incoming message from remote server
        data = sock.recv(RECV_BUFFER)
        if not data:
            print '\nNgắt kết nối từ Server!!!'
            sys.exit()
        else:
            sys.stdout.write(data + '\n>')
            # clean cache
            sys.stdout.flush()
    else:
        # user entered a message
        sys.stdout.write('>')
        sys.stdout.flush()

        # recv data from keyboard
        msg_content = sys.stdin.readline().strip()
        s.send(msg_content)

        if '#exit' in msg_content:
            print "GoodBye!!!"
            sys.exit()

def make_new_user():
    user_name = raw_input("Nhập nick_name: ")
    if is_ascii(user_name):
        return [True, user_name]
    return [False, user_name]
