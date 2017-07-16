# server chat
# -*- coding: utf-8 -*-

import sys
sys.path.append("lib")

import time
import select
import socket
import os
from ServerSupport import *
from ProcessSupport import *

RECV_BUFFER = 4096

def make_server_chat():
    server        = Server()
    server_socket = server.bind_a_server()
    transfer      = server.transfer_data_to_client()

    # add server socket object to the list of readable connections
    SOCKET_LIST.append(server_socket)

    try:
        while True:
            # get the list sockets which are ready to be read through select
            # 4th arg, time_out  = 0 : poll and never block
            ready_to_read, ready_to_write, in_error = select.select(
                SOCKET_LIST, [], [], 0)

            for sock in ready_to_read:
                # a new connection request recieved
                if sock == server_socket:
                    sockfd, addr = server_socket.accept()
                    SOCKET_LIST.append(sockfd)

                # a message from a client, not a new connection
                else:
                    try:
                        # receiving data from the socket.
                        recv_data = sock.recv(RECV_BUFFER)
                        if recv_data != "" or len(recv_data) > 1:
                            # handle data,  send to client
                            server.handle_data_from_client(
                                server_socket, transfer, sock, recv_data)
                        else:
                            # remove the socket that's broken or client
                            if sock in SOCKET_LIST:
                                content_message = msg_user_logout(user_name, sock)
                                SOCKET_LIST.remove(sock)

                            # at this stage, no data means probably the
                            # connection has been broken
                            server.broadcast(
                                server_socket, sock, content_message)
                            continue

                    except BaseException as e:
                        print "Error", e
                        content_message = msg_user_logout(user_name, sock)
                        server.broadcast(
                            server_socket, sock, content_message)
                        continue
    except BaseException as e:
        print "Error", e
        print "----------------------------------------------------------"
        content_message = msg_server_status("off")
        show(content_message)


if __name__ == "__main__":
    sys.exit(make_server_chat())
