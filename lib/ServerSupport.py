# server class
# -*- coding: utf-8 -*-

from ProcessSupport import *
import socket
import time
import os

SOCKET_LIST   = []
server_socket = None
user_name     = {}
transfer      = None
PORT          = 8888
USER_MAX      = 10  # number of users in a channel
TIME_OUT      = 2


class Server:
    def __init__(self):
        os.system('clear')
        self.server_host    = ''
        self.current_server = "1"

    # bind server
    def bind(self, user_max):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.server_host, PORT))
        server_socket.listen(user_max)

        return server_socket

    def bind_a_server(self):
        try:
            msg_bind_server(PORT)
            server_socket = self.bind(USER_MAX)

        except BaseException as e:
            print "Error", e
            return None

        else:
            msg_server_status("on")
            msg_server_online()
            draw_line()

            return server_socket

    # broadcast chat messages to all connected clients
    def broadcast(self, server_socket, sock, message):
        for socket in SOCKET_LIST:
            # send the message only to peer
            if socket != server_socket and socket != sock:
                try:
                    socket.send(message)
                except BaseException as e:
                    print "Error", e
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)

    def transfer_data_to_client(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIME_OUT)
        try:
            s.connect((self.server_host, PORT))
        except BaseException as e:
            print "Error", e
            return None
        else:
            return s

    # Send messages to 1 connected client
    def server_send_to_client(
            self,
            server_socket,
            transfer,
            sock,
            message):
        for socket in SOCKET_LIST:
            # send the message only to peer
            if socket != server_socket and socket != transfer:
                try:
                    if message: socket.send(message)
                except BaseException as e:
                    print "Error", e
                    # broken socket connection
                    socket.close()
                    # broken socket, remove it
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)

    # Xu li Recvdata chua thong so
    def handle_data_from_client(
            self,
            server_socket,
            transfer,
            sock,
            recv_data):
        new_socker_server = server_socket
        new_transfer = transfer
        new_socker = sock

        if "#user" in recv_data:
            new_user_name = recv_data.split(":")[1].strip()
            for key, value in user_name.items():
                if new_user_name in value:
                    new_user_name = value + str(1)

            user_name[new_socker.getpeername()] = new_user_name
            count_users_online = msg_count_user_online(user_name)
            user_msg = msg_count_new_user(
                new_socker,
                new_user_name,
                self.current_server)

            message_content = user_msg[1]
            print user_msg[0]
            print count_users_online

            self.server_send_to_client(
                new_socker_server,
                new_transfer,
                new_socker,
                message_content)
            self.server_send_to_client(
                new_socker_server,
                new_transfer,
                new_socker,
                count_users_online)

        elif "#m" in recv_data:
            print "music:"
            message_content = Msg.INTRO
            print message_content
            try:
                self.server_send_to_client(
                    new_socker_server, new_transfer, new_socker, message_content)
            except BaseException as e:
                print "Error", e
                pass

        elif "#exit" in recv_data:
            try:
                msg_usr_logout = msg_user_logout(user_name, new_socker)

            except BaseException as e:
                print "Error", e
                print "Error when exit"

            else:
                # send data to Client
                message_content = msg_usr_logout[1]
                remove_user_from_chat(user_name, new_socker)
                count_users_online = msg_count_user_online(user_name)

                print msg_usr_logout[0]
                print count_users_online

                self.broadcast(
                    new_socker_server, new_socker, message_content)
                self.broadcast(
                    new_socker_server,
                    new_socker,
                    count_users_online)
                SOCKET_LIST.remove(new_socker)

        # recv data, broadcast
        else:
            try:
                message_content = msg_handle_user(
                    user_name, new_socker, recv_data)
                self.broadcast(
                    new_socker_server, new_socker, message_content)
                print message_content
            except BaseException as e:
                print "Error", e
